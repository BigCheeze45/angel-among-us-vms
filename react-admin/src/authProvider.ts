import jwt_decode from "jwt-decode"
import {AuthProvider} from "react-admin"
import {TokenStore, UserPayload, localStorageTokenStore, googleAuthProvider, IdConfiguration} from "ra-auth-google"
import {API_BASE_URL} from "./constants"

/**
 * Returns an extended googleAuthProvider that can be used with react-admin.
 * @param gsiParams **Required** - Parameters for the Google Identity Services library.
 * @param tokenStore *Optional* - The token store to use to store the token. Defaults to localStorageTokenStore.
 */

export const authProvider = ({
  gsiParams,
  tokenStore = localStorageTokenStore,
}: {
  gsiParams: Omit<IdConfiguration, "callback">
  tokenStore?: TokenStore
}): AuthProvider => {
  const baseAuthProvider = googleAuthProvider({gsiParams, tokenStore})

  return {
    async login(params) {
      await baseAuthProvider.login(params)
      const googleToken = tokenStore?.getToken()
      const user: UserPayload = jwt_decode(googleToken)

      const authString = `${user.email}:${""}`
      const response = await fetch(`${API_BASE_URL}/api/auth/login/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Basic " + btoa(authString),
        },
      })

      if (!response.ok) {
        const body = await response.json()
        throw new Error(body.detail)
      }

      const data = await response.json()
      localStorage.setItem("apiToken", data.token)
      localStorage.setItem("permissions", JSON.stringify(data.user.permissions))
    },

    async logout(params) {
      await baseAuthProvider.logout(params)
      localStorage.removeItem("permissions")
      try {
        const apiToken = localStorage.getItem("apiToken")
        await fetch(`${API_BASE_URL}/api/auth/logout/`, {
          method: "POST",
          headers: {Authorization: `Token ${apiToken}`},
        })
        localStorage.removeItem("apiToken")
      } catch (error) {
        console.log(error)
      }
    },
    async canAccess({action, resource, record}) {
      console.log("canAccess")
      const permissions = JSON.parse(localStorage.getItem('permissions'))
      console.log(permissions)
      return permissions.some(p =>
        p.resource === resource && p.action.includes(action)
      )
    },
    async checkAuth(params) {
      console.log("checkAuth")
      const apiToken = localStorage.getItem("apiToken")
      if (!apiToken) {
        throw new Error("Session expired. Please login.")
      }
      // console.log(apiToken)

      // const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/api/auth/validate-token/`, {
      //     method: 'POST',
      //     headers: {
      //         Authorization: `Bearer ${apiToken}`,
      //     },
      // });

      // if (!response.ok) {
      //     throw new Error('Invalid API token.');
      // }

      // return Promise.resolve();
    },

    async checkError(error) {
        const status = error.status;
        if (status === 401) {
            localStorage.removeItem('apiToken');
            return Promise.reject();
        }
        return Promise.resolve();
    },

    async getPermissions(params) {
      console.log("getPermissions")
      const permissions = JSON.parse(localStorage.getItem("permissions"))
      if (!permissions) {
        throw new Error("No API token found")
      }
      // console.log(permissions)
      return permissions
    },
  }
}
