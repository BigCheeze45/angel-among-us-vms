import {Show, TabbedShowLayout, TextField, BooleanField, DateField, EmailField} from "react-admin"

export const UserShow = () => (
  <Show>
    <TabbedShowLayout>
      <TabbedShowLayout.Tab label="summary">
        <TextField source="first_name" />
        <TextField source="last_name" />
        <EmailField source="email" />
        <BooleanField source="is_staff" />
        <TextField source="role" />
        <BooleanField source="is_active" />
        <DateField source="last_login" />
        <DateField source="date_joined" />
      </TabbedShowLayout.Tab>
    </TabbedShowLayout>
  </Show>
)
