import {Create, SimpleForm, TextInput, BooleanInput, PasswordInput} from "react-admin"

export const UserCreate = () => (
  <Create>
    <SimpleForm>
      <TextInput
        source="first_name"
        label="First Name"
      />
      <TextInput
        source="last_name"
        label="Last Name"
      />
      <TextInput
        source="username"
        label="Username"
      />
      <TextInput
        source="email"
        label="Email"
      />
      <PasswordInput source="password" />
      <BooleanInput
        source="is_superuser"
        label="Superuser"
      />
      <BooleanInput
        source="is_staff"
        label="Staff"
      />
      <BooleanInput
        source="is_active"
        label="Active"
      />
      {/* <DateInput source="date_joined" label="Date Joined" /> */}
    </SimpleForm>
  </Create>
)
