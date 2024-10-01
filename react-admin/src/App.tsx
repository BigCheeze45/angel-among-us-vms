import {
  Admin,
  Resource,
  EditGuesser,
  BulkDeleteButton,
  BulkExportButton,
  BulkUpdateButton,
  ShowGuesser,
  List,
  TextField,
  UrlField,
  EmailField,
  BooleanField,
  Datagrid,
} from "react-admin"
import {Fragment} from "react"
import {Layout} from "./Layout"
import dataProvider from "./dataProvider"

const drfProvider = dataProvider()

const PostBulkActionButtons = () => (
  <Fragment>
    <BulkExportButton />
    <BulkUpdateButton data={{is_staff: true}} />
    <BulkDeleteButton />
  </Fragment>
)

const UserList = () => (
  <List>
    <Datagrid bulkActionButtons={<PostBulkActionButtons />}>
      {/* <TextField source="id" /> */}
      {/* <UrlField source="url" /> */}
      <TextField source="username" />
      <EmailField source="email" />
      <BooleanField source="is_staff" />
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
      list={UserList}
      show={ShowGuesser}
      edit={EditGuesser}
    />
    <Resource name="team/category" />
  </Admin>
)
