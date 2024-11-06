import {
  List,
  DateField,
  TopToolbar,
  TextField,
  EmailField,
  FilterButton,
  BooleanField,
  ReferenceInput,
  AutocompleteInput,
  SelectColumnsButton,
  DatagridConfigurable,
} from "react-admin"
import {Fragment} from "react"
import {GA_COUNTIES} from "../../constants"
import {ExportCSVButton} from "../../components/ExportCSVButton"
import {VolunteerFilterSidebar} from "./VolunteersFilterSidebar"
import {ExportExcelButton} from "../../components/ExportExcelButton"

const volunteerFilters = [
  <ReferenceInput
    key="team_filter"
    source="team_id"
    reference="teams"
    perPage={25}
    sort={{field: "name", order: "ASC"}}
  />,
  <AutocompleteInput
    key="county_filter"
    source="county"
    choices={GA_COUNTIES}
  />,
  // <DateInput key="date_joined_filter" source="date_joined" />,
]

const VolunteersListActions = () => (
  <TopToolbar>
    <FilterButton />
    <ExportCSVButton />
    <ExportExcelButton />
    <SelectColumnsButton />
  </TopToolbar>
)

const VolunteerBulkActionButtons = () => (
  <Fragment>
    <ExportCSVButton />
    <ExportExcelButton />
  </Fragment>
)

export const VolunteersList = () => (
  <List
    filters={volunteerFilters}
    actions={<VolunteersListActions />}
    aside={<VolunteerFilterSidebar />}
  >
    <DatagridConfigurable bulkActionButtons={<VolunteerBulkActionButtons />} omit={["active_status_change_date", "date_of_birth", "maddie_certifications_received_date"]}>
      <TextField
        source="full_name"
        label="Name"
      />
      <TextField source="preferred_name" />
      <EmailField source="email" />
      <DateField source="date_joined" />
      <DateField source="active_status_change_date" />
      <BooleanField source="active" />
      <TextField source="cell_phone" />
      <DateField source="date_of_birth" label="Birth date" />
      <TextField source="job_title" />
      <DateField source="application_received_date" showTime label="Last updated" />
      <DateField source="maddie_certifications_received_date" label="Maddie certification date" />
      {/* <TextField source="first_name" /> */}
      {/* <TextField source="middle_name" /> */}
      {/* <TextField source="last_name" /> */}
      {/* <TextField source="home_phone" /> */}
      {/* <TextField source="work_phone" /> */}
    </DatagridConfigurable>
  </List>
)
