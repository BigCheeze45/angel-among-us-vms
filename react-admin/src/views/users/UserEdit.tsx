import {BooleanInput, Edit, SimpleForm, SelectInput, choices, TextInput} from "react-admin"

export const UserEdit = () => {
  return (
    <Edit>
      <SimpleForm>
        <TextInput source="first_name" />
        <TextInput source="last_name" />
        <TextInput source="email" />
        {/* <SelectInput
          source="roles"
          label="Role"
          required={true}
          validate={choices(["administrator", "editor", "viewer"], "Please choose one of the values")}
          // defaultValue="viewer"
          choices={[
            {id: "administrator", name: "Administrator"},
            {id: "viewer", name: "Viewer"},
            {id: "editor", name: "Editor"},
          ]}
        /> */}
        <BooleanInput
          source="is_staff"
          label="Staff"
          helperText="Designates whether the user can log into this admin site."
        />
        <BooleanInput
          source="is_active"
          label="Active"
          helperText="Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        />
      </SimpleForm>
    </Edit>
  )
}
