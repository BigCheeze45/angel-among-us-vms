import {Admin, Resource} from "react-admin"
import {Layout} from "./Layout"
import dataProvider from "./dataProvider"
import {TeamShow} from "./views/teams/TeamShow"
import {UserShow} from "./views/users/UserShow"
import {UsersList} from "./views/users/UserList"
import {UserEdit} from "./views/users/UserEdit"
import {TeamList} from "./views/teams/TeamsList"
import {VolunteerShow} from "./views/volunteers/VolunteerShow"
import {VolunteersList} from "./views/volunteers/VolunteersList"

const drfProvider = dataProvider()

export const App = () => (
  <Admin
    layout={Layout}
    dataProvider={drfProvider}
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
      list={UsersList}
      edit={UserEdit}
      // display user full name when presenting a record (e.g. show view)
      recordRepresentation={record => `${record.first_name} ${record.last_name}`}
    />
  </Admin>
)
