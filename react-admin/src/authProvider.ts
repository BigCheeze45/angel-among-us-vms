import jwt_decode from "jwt-decode"
import {API_BASE_URL} from "./constants"
import inMemoryTokenStore from "./tokenStore"
import {TokenStore, UserPayload} from "ra-auth-google"
import {AuthProvider, QueryFunctionContext, HttpError} from "react-admin"

export default (baseAuthProvider: AuthProvider, tokenStore: TokenStore): AuthProvider => ({
  login: async function (params) {
    // Google SSO login
    // Only one auto re-authn request can be made every 10 minutes.
    await baseAuthProvider.login(params)
    const googleToken = tokenStore?.getToken()

    const response = await fetch(`${API_BASE_URL}/api/auth/login/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // Authorization: "Basic " + btoa(`${user.email}:${""}`),
        Authorization: "Basic " + btoa(`${googleToken}:${""}`),
      },
    })

    if (!response.ok) {
      const body = await response.json()
      return Promise.reject({message: body.detail || response.statusText})
    }

    const data = await response.json()
    inMemoryTokenStore.setToken(data.token)
    localStorage.setItem("permissions", JSON.stringify(data.user.permissions))
    // remove G token it's no longer needed
    tokenStore?.removeToken()
  },
  logout: async function (params): Promise<void | false | string> {
    // log out of Google SSO
    await baseAuthProvider.logout(params)

    // delete token from backend if it's still valid
    const apiToken = inMemoryTokenStore.getToken()
    await fetch(`${API_BASE_URL}/api/auth/logout/`, {
      method: "POST",
      headers: {Authorization: `Token ${apiToken}`},
    })

    // clean up client side
    inMemoryTokenStore.removeToken()
    localStorage.removeItem("permissions")
  },
  checkAuth: async function (params: any & QueryFunctionContext): Promise<void> {
    const apiToken = inMemoryTokenStore.getToken()
    console.log(apiToken)
    if (!apiToken) {
      // No access token present
      return Promise.reject({message: "Session expired. Please login."})
    }

    // #region Try to refresh the token
    const response = await fetch(`${API_BASE_URL}/api/auth/refresh/`, {
      method: "POST",
      headers: {Authorization: `Token ${apiToken}`},
    })

    if (!response.ok) {
      // token has expired completely user needs to sign
      return Promise.reject({message: "Session expired. Please login."})
    }
    // #endregion
  },
  checkError: async function (error: any): Promise<void> {
    const status = error.status
    if (status === 401) {
      inMemoryTokenStore.removeToken()
      return Promise.reject({message: "Session expired. Please login."})
    }
  },
  getIdentity: async function () {
    // get user's Google identity (name, profile pic)
    return await baseAuthProvider.getIdentity()
  },
  canAccess: async function ({action, resource, _record}) {
    const permissions = JSON.parse(localStorage.getItem("permissions"))
    return permissions.some(p => p.resource === resource && p.action.includes(action))
  },
  getPermissions: async function (params) {
    const permissions = JSON.parse(localStorage.getItem("permissions"))
    if (!permissions) {
      // no permissions found. Assume user doesn't have any permissions
      throw new HttpError("Forbidden", 403)
    }
    return permissions
  },
})
