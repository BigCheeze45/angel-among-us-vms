import jwt_decode from 'jwt-decode'
import { AuthProvider } from 'react-admin'
import { TokenStore, UserPayload, localStorageTokenStore, googleAuthProvider, CredentialResponse, IdConfiguration } from 'ra-auth-google'

/**
 * Returns an extended googleAuthProvider that can be used with react-admin.
 * 
 * Based on ra-auth-google:
 * https://marmelab.com/react-admin/AuthProviderList.html
 *
 * @param gsiParams **Required** - Parameters for the Google Identity Services library. See the [documentation](https://developers.google.com/identity/gsi/web/reference/js-reference?hl=en#IdConfiguration) for the full list of supported parameters.
 * @param tokenStore *Optional* - The token store to use to store the token. Defaults to `localStorageTokenStore`.
 *
 * @example
 * ```ts
 * const authProvider = googleAuthProvider({
 *   gsiParams: {
 *     client_id: "my-application-client-id.apps.googleusercontent.com",
 *     ux_mode: "popup",
 *   },
 *   tokenStore: myTokenStore,
 * });
 * ```
 */
export const authProvider = ({
    gsiParams,
    tokenStore = localStorageTokenStore
}: {
    gsiParams: Omit<IdConfiguration, 'callback'>;
    tokenStore?: TokenStore;
}): AuthProvider => {
    const baseAuthProvider = googleAuthProvider({ gsiParams, tokenStore });

    return {
        ...baseAuthProvider,

        async login(params) {
            // wait for Google login to finish
            await baseAuthProvider.login(params)
            // user successfully signed in with Google
            
            // const googleToken = tokenStore?.getToken()
            // const user: UserPayload = jwt_decode(googleToken)

            // TODO: call backend to generate an API token
            // React-admin expects this async method to return if the login
            // data is correct, OR throw an error if it’s not.
            // https://marmelab.com/react-admin/AuthProviderWriting.html
            throw new Error('Failed to handle login.')
        },
        async logout(params) {
            // wait for Google logout to finish
            await baseAuthProvider.logout(params)
            // Google logout successfully

            // TODO: 1: call backend to destroy token
            //       2: clean up client side
        },
        
        async checkAuth(params) {
            const result = await baseAuthProvider.checkAuth(params)
            // Add any additional checks/logic here if needed
            return result
        },

        async checkError(error) {
            const result = await baseAuthProvider.checkAuth(error);
            // Add any additional checks/logic here if needed
            return result
        },

        async getPermissions(params) {
            // TODO: retrieve user permissions that were provided
            //       and saved upon logging in
            // https://marmelab.com/react-admin/Permissions.html#permissions
            return []
        },
        // Override getIdentity to fetch more user details if needed
        // async getIdentity(params) {
        //     const baseIdentity = await baseAuthProvider.getIdentity(params)
        //     // Example: Fetch additional user details from your API
        //     // const additionalDetails = await fetchAdditionalUserDetails(baseIdentity.id);
        //     // return { ...baseIdentity, ...additionalDetails };
        //     return baseIdentity
        // },
    };
}
