import {
  Admin,
  Resource,
  EditGuesser,
  BulkDeleteButton,
  BulkExportButton,
  BulkUpdateButton,
  ShowGuesser,
  ListGuesser,
  List,
  TextField,
  EmailField,
  BooleanField,
  DateField,
  NumberField,
  ReferenceField,
  Datagrid,
} from "react-admin"
import { Fragment } from "react"
import { Layout } from "./Layout"
import dataProvider from "./dataProvider"
import { VolunteersCreate }  from "./components/VolunteersCreate.tsx" //This is added from Teodora.
import React from 'react'
import CustomExportButton from "./components/CustomExportButton"

const drfProvider = dataProvider()

const PostBulkActionButtons = () => (
  <Fragment>
    <BulkExportButton />
    <BulkUpdateButton data={{ active: false }} />
    <BulkDeleteButton />
  </Fragment>
)

const VolunteerList: React.FC = (props) => (
  <List {...props} actions={<CustomExportButton/>}> {/* Custom Export Button */}
  
    <Datagrid bulkActionButtons={<PostBulkActionButtons />}>
      {/* <TextField source="id" /> */}
      {/* <TextField source="first_name" /> */}
      {/* <TextField source="middle_name" /> */}
      {/* <TextField source="last_name" /> */}
      <TextField source="full_name" label="Name" />
      {/* <TextField source="preferred_name" /> */}
      <EmailField source="email" />
      <DateField source="date_joined" />
      <DateField source="active_status_change_date" />
      {/* <DateField source="created_at" /> */}
      <BooleanField source="active" />
      <TextField source="cell_phone" />
      {/* <TextField source="home_phone" /> */}
      {/* <TextField source="work_phone" /> */}
      <DateField source="date_of_birth" />
      <TextField source="ishelters_category_type" />
      <BooleanField source="ishelters_access_flag" />
      {/* <ReferenceField source="ishelters_id" reference="ishelters" /> */}
      <DateField source="maddie_certifications_received_date" />
      {/* <NumberField source="created_by" /> */}
      {/* <NumberField source="address" /> */}
    </Datagrid>
  </List>
)

const UserList = () => (
  <List>
    <Datagrid>
      {/* <TextField source="id" /> */}
      {/* <DateField source="password" /> */}
      <TextField source="first_name" />
      <TextField source="last_name" />
      <TextField source="username" />
      <EmailField source="email" />
      <BooleanField source="is_superuser" />
      <BooleanField source="is_staff" />
      <BooleanField source="is_active" />
      <TextField source="last_login" />
      <DateField source="date_joined" />
      {/* <TextField source="groups" /> */}
      {/* <TextField source="user_permissions" /> */}
    </Datagrid>
  </List>
)

export const App = () => (
  <Admin
    layout={Layout}
    dataProvider={drfProvider}
  >
    <Resource
      name="volunteers"
      // list={ListGuesser}
      list={VolunteerList}
      show={ShowGuesser}
      edit={EditGuesser}
      create={VolunteersCreate} //This is added from Teodora.
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
    />
    {/* <Resource name="team/category" /> */}
  </Admin>
)
