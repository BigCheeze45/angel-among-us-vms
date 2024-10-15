import {
  Admin,
  Resource,
  EditGuesser,
  ShowGuesser,
  ListGuesser,
} from "react-admin";
import { Layout } from "./Layout";
import dataProvider from "./dataProvider";
import { UserCreate } from "./components/UserCreate";
import { UserList } from "./views/users/UserList";
import { VolunteerShow } from "./views/volunteers/VolunteerShow";
import { VolunteersList } from "./views/volunteers/VolunteersList";

const drfProvider = dataProvider();

export const App = () => (
  <Admin
    layout={Layout}
    dataProvider={drfProvider}
  >
    <Resource
      name="volunteers"
      show={VolunteerShow}
      list={VolunteersList}
      recordRepresentation={(record) => `${record.full_name}`}
    />
    <Resource
      name="teams"
      list={ListGuesser}
      show={ShowGuesser}
      edit={EditGuesser}
    />
    <Resource
      name="users"
      list={UserList}
      show={ShowGuesser}
      edit={EditGuesser}
      create={UserCreate} 
    />
  </Admin>
);
