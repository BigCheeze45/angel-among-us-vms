import {BooleanField, UrlField, DateField, EmailField, Show, SimpleShowLayout, TextField} from "react-admin"

export const ShowSummary = () => (
  <Show
    title={false}
    actions={false}
  >
    <SimpleShowLayout>
      <TextField source="full_name" />
      <TextField source="preferred_name" />
      <TextField source="first_name" />
      <TextField source="middle_name" />
      <TextField source="last_name" />
      <TextField source="job_title" />
      <DateField source="date_joined" />
      <EmailField source="email" />
      <TextField source="cell_phone" />
      <TextField source="home_phone" />
      <TextField source="work_phone" />
      <BooleanField source="active" />
      <DateField source="date_of_birth" />
      <DateField
        label="Maddie certification date"
        source="maddie_certifications_received_date"
      />
      <UrlField
        target="_blank"
        rel="noopener noreferrer"
        source="ishelters_profile"
        label="iShelters Profile"
        content="View iShelters profile"
      />
      <DateField
        showTime
        label="Last updated"
        source="application_received_date"
      />
    </SimpleShowLayout>
  </Show>
)
