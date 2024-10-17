import {BooleanInput, PasswordInput, Edit, SimpleForm, TextInput} from "react-admin"

export const UserEdit = () => (
  <Edit>
    <SimpleForm>
      <TextInput source="first_name" />
      <TextInput source="last_name" />
      <TextInput source="username" />
      <TextInput source="email" />
      <PasswordInput source="password" />
      <BooleanInput source="is_superuser" />
      <BooleanInput source="is_staff" />
      <BooleanInput source="is_active" />
      {/* <TextInput source="id" /> */}
      {/* <DateInput source="date_joined" /> */}
      {/* <TextInput source="last_login" /> */}
      {/* <TextInput source="groups" /> */}
      {/* <TextInput source="user_permissions" /> */}
    </SimpleForm>
  </Edit>
)
