import {Layout} from "./Layout"
import {LoginPage} from "./pages/Login"
import dataProvider from "./dataProvider"
import {Admin, Resource} from "react-admin"
import {GOOGLE_CLIENT_ID} from "./constants"
import {TeamShow} from "./views/teams/TeamShow"
import {UserShow} from "./views/users/UserShow"
import {UsersList} from "./views/users/UserList"
import {UserEdit} from "./views/users/UserEdit"
import {TeamList} from "./views/teams/TeamsList"
import {VolunteerShow} from "./views/volunteers/VolunteerShow"
import {VolunteersList} from "./views/volunteers/VolunteersList"
import {useGoogleAuthProvider, GoogleAuthContextProvider, localStorageTokenStore} from "ra-auth-google"
// import authProvider from "./authProvider_two"
import {authProvider} from "./authProvider"

export const App = () => {
  // configure Sign-in with Google
  const {gsiParams, authProvider: googleAuthProvider} = useGoogleAuthProvider({
    client_id: GOOGLE_CLIENT_ID,
  })
  const drfDataProvider = dataProvider()
  // wrap out auth provider around Google
  // const drfAuthProvider = authProvider(googleAuthProvider)
  const drfAuthProvider = authProvider(gsiParams)

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
