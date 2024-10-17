import {Show, TabbedShowLayout, TextField, BooleanField, DateField, EmailField} from "react-admin"

export const UserShow = () => (
  <Show>
    <TabbedShowLayout>
      <TabbedShowLayout.Tab label="summary">
        <TextField source="first_name" />
        <TextField source="last_name" />
        <EmailField source="email" />
        <TextField source="username" />
        <BooleanField source="is_superuser" />
        <BooleanField source="is_staff" />
        <BooleanField source="is_active" />
        <DateField source="last_login" />
        <DateField source="date_joined" />
        {/* <DateField source="password" /> */}
        {/* <TextField source="id" /> */}
      </TabbedShowLayout.Tab>
      {/* <TabbedShowLayout.Tab label="address">
                <TextField source='address_line_1' />
                <TextField source='address_line_2' />
                <TextField source='city' />
                <TextField source='state' />
                <TextField source='county' />
                <TextField source='zipcode' />
            </TabbedShowLayout.Tab> */}
    </TabbedShowLayout>
  </Show>
)
