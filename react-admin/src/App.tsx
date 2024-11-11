import {Layout} from "./Layout"
import {LoginPage} from "./pages/Login"
import dataProvider from "./dataProvider"
import {GOOGLE_CLIENT_ID} from "./constants"
import {TeamShow} from "./views/teams/TeamShow"
import {UserShow} from "./views/users/UserShow"
import {UsersList} from "./views/users/UserList"
import {UserEdit} from "./views/users/UserEdit"
import {TeamList} from "./views/teams/TeamsList"
import {Admin, Resource, EditGuesser} from "react-admin"
import {VolunteerEdit} from "./views/volunteers/VolunteerEdit"
import {VolunteersList} from "./views/volunteers/VolunteersList"
import {VolunteerShow} from "./views/volunteers/show/VolunteerShow"
import {useGoogleAuthProvider, GoogleAuthContextProvider} from "ra-auth-google"

export const App = () => {
  const drfProvider = dataProvider()
  const {authProvider, gsiParams} = useGoogleAuthProvider({
    client_id: GOOGLE_CLIENT_ID,
  })

  return (
    <GoogleAuthContextProvider value={gsiParams}>
      <Admin
        // https://marmelab.com/react-admin/Admin.html#requireauth
        requireAuth
        layout={Layout}
        loginPage={LoginPage}
        dataProvider={drfProvider}
        authProvider={authProvider}
      >
        <Resource
          name="volunteers"
          show={VolunteerShow}
          list={VolunteersList}
          edit={VolunteerEdit}
          hasCreate={false}
          recordRepresentation={record => `${record.full_name}`}
        />
        <Resource
          name="teams"
          list={TeamList}
          show={TeamShow}
          edit={EditGuesser}
          // hasEdit={false}
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
