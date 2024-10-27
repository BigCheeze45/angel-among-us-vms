import { Show, TabbedShowLayout, TextField, BooleanField, DateField, EmailField } from "react-admin"

export const UserShow = () => (
  <Show>
    <TabbedShowLayout>
      <TabbedShowLayout.Tab label="summary">
        <TextField source="first_name" />
        <TextField source="last_name" />
        <EmailField source="email" />
        <BooleanField source="is_superuser" />
        <BooleanField source="is_staff" />
        <BooleanField source="is_active" />
        <DateField source="last_login" />
        <DateField source="date_joined" />
        {/* <TextField source="id" /> */}
      </TabbedShowLayout.Tab>
      {/* <TabbedShowLayout.Tab label="address">
                <TextField source='address_line_1' />
                <TextField source='address_line_2' />
                <TextField source='zipcode' />
                <TextField source='city' />
                <TextField source='state' />
                <TextField source='county' />
            </TabbedShowLayout.Tab> */}
    </TabbedShowLayout>
  </Show>
)
