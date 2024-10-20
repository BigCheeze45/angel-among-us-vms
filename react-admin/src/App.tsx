import {Layout} from "./Layout"
import {LoginPage} from "./pages/Login"
import dataProvider from "./dataProvider"
import {authProvider} from "./authProvider"
import {Admin, Resource} from "react-admin"
import {TeamShow} from "./views/teams/TeamShow"
import {UserShow} from "./views/users/UserShow"
import {UsersList} from "./views/users/UserList"
import {UserEdit} from "./views/users/UserEdit"
import {TeamList} from "./views/teams/TeamsList"
import {UserCreate} from "./views/users/UserCreate"
import {VolunteerShow} from "./views/volunteers/VolunteerShow"
import {VolunteersList} from "./views/volunteers/VolunteersList"
import {useGoogleAuthProvider, GoogleAuthContextProvider} from "ra-auth-google"

export const App = () => {
  const drfProvider = dataProvider()
  
  // configure Sign-in with Google
  const { gsiParams } = useGoogleAuthProvider({
    client_id: import.meta.env.VITE_GOOGLE_CLIENT_ID,
  })
  // an extended googleAuthProvider that handles login callback
  const drfAuthProvider = authProvider(gsiParams)

  return (
    <GoogleAuthContextProvider value={gsiParams}>
      <Admin
        // https://marmelab.com/react-admin/Admin.html#requireauth
        requireAuth
        layout={Layout}
        loginPage={LoginPage}
        dataProvider={drfProvider}
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
          create={UserCreate}
          // display user full name when presenting a record (e.g. show view)
          recordRepresentation={record => `${record.first_name} ${record.last_name}`}
        />
      </Admin>
    </GoogleAuthContextProvider>
  )
}
