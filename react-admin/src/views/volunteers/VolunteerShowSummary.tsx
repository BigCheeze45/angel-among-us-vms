import {BooleanField, DateField, EmailField, ReferenceField, Show, SimpleShowLayout, TextField} from "react-admin"

export const VolunteerShowSummary = () => (
  <Show title={false}>
    <SimpleShowLayout>
      <TextField source="first_name" />
      <TextField source="middle_name" />
      <TextField source="last_name" />
      <TextField source="full_name" />
      <TextField source="preferred_name" />
      <EmailField source="email" />
      <DateField source="date_joined" />
      <DateField source="active_status_change_date" />
      <DateField source="created_at" />
      <BooleanField source="active" />
      <TextField source="cell_phone" />
      <TextField source="home_phone" />
      <TextField source="work_phone" />
      <DateField source="date_of_birth" />
      <TextField source="ishelters_category_type" />
      <BooleanField source="ishelters_access_flag" />
      <DateField source="maddie_certifications_received_date" />
      <BooleanField source="has_maddie_certifications" />
      <ReferenceField
        source="created_by"
        reference="users"
        label="Added by"
      >
        <TextField source="first_name" />
        <TextField source="last_name" />
      </ReferenceField>
    </SimpleShowLayout>
  </Show>
)
