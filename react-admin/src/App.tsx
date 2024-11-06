import {Layout} from "./Layout"
import {LoginPage} from "./pages/Login"
import dataProvider from "./dataProvider"
import authProvider from "./authProvider"
import {Admin, Resource} from "react-admin"
import {GOOGLE_CLIENT_ID} from "./constants"
import {TeamShow} from "./views/teams/TeamShow"
import {UserShow} from "./views/users/UserShow"
import {UserEdit} from "./views/users/UserEdit"
import {UsersList} from "./views/users/UserList"
import {TeamList} from "./views/teams/TeamsList"
import {VolunteerShow} from "./views/volunteers/VolunteerShow"
import {VolunteersList} from "./views/volunteers/VolunteersList"
import {useGoogleAuthProvider, GoogleAuthContextProvider, localStorageTokenStore} from "ra-auth-google"

export const App = () => {
  // configure Sign-in with Google
  // Only one auto re-authn request can be made every 10 minutes.
  const {gsiParams, authProvider: googleAuthProvider} = useGoogleAuthProvider({
    auto_select: true,
    itp_support: true,
    use_fedcm_for_prompt: true,
    client_id: GOOGLE_CLIENT_ID,
    cancel_on_tap_outside: false,
    tokenStore: localStorageTokenStore,
  })
  const drfDataProvider = dataProvider()
  // wrap out auth provider around Google's, making sure to provide they're using
  // the same token store
  const drfAuthProvider = authProvider(googleAuthProvider, localStorageTokenStore)

  return (
    <GoogleAuthContextProvider value={gsiParams}>
      <Admin
        // https://marmelab.com/react-admin/Admin.html#requireauth
        requireAuth
        layout={Layout}
        loginPage={LoginPage}
        dataProvider={drfDataProvider}
        authProvider={drfAuthProvider}
      >
        <Resource
          name="volunteers"
          show={VolunteerShow}
          list={VolunteersList}
          hasEdit={false}
          hasCreate={false}
          recordRepresentation={record => `${record.full_name}`}
        />
        <Resource
          name="teams"
          list={TeamList}
          show={TeamShow}
          hasEdit={false}
          hasCreate={false}
        />
        <Resource
          name="users"
          show={UserShow}
          edit={UserEdit}
          list={UsersList}
          /*
            There is a Create view however it's a dialog that's only available
            from UsersList. Setting this to false so RA doesn't doesn't
            do anything unexpected (e.g. trying to navigate to it)
          */
          hasCreate={false}
          // display user full name when presenting a record (e.g. show view)
          recordRepresentation={record => `${record.first_name} ${record.last_name}`}
        />
      </Admin>
    </GoogleAuthContextProvider>
  )
}
