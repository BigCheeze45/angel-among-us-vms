import {
  List,
  DateField,
  TextField,
  EmailField,
  BooleanField,
  ReferenceInput,
  AutocompleteInput,
  DatagridConfigurable,
  BulkExportButton,
  TopToolbar,
  ExportButton,
  FilterButton,
  SelectColumnsButton,
} from "react-admin"
import {Fragment} from "react"
import {GA_COUNTIES} from "../../constants"
import {VolunteerFilterSidebar} from "./VolunteersFilterSidebar"
import ExportExcelButton from "../../components/ExportExcelButton"

const volunteerFilters = [
  <ReferenceInput
    key="team_filter"
    source="team_id"
    reference="teams"
    perPage={150}
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
    <ExportButton label="export csv" />
    <ExportExcelButton />
    <SelectColumnsButton />
  </TopToolbar>
)

const VolunteerBulkActionButtons = () => (
  <Fragment>
    <BulkExportButton label="export csv" />
    <ExportExcelButton />
  </Fragment>
)

export const VolunteersList = () => (
  <List
    filters={volunteerFilters}
    actions={<VolunteersListActions />}
    aside={<VolunteerFilterSidebar />}
  >
    <DatagridConfigurable bulkActionButtons={<VolunteerBulkActionButtons />}>
      <TextField
        source="full_name"
        label="Name"
      />
      <EmailField source="email" />
      <DateField source="date_joined" />
      <DateField source="active_status_change_date" />
      <BooleanField source="active" />
      <TextField source="cell_phone" />
      <DateField source="date_of_birth" />
      <TextField source="ishelters_category_type" />
      <BooleanField source="ishelters_access_flag" />
      <DateField source="maddie_certifications_received_date" />
      {/* <TextField source="id" /> */}
      {/* <TextField source="first_name" /> */}
      {/* <TextField source="middle_name" /> */}
      {/* <TextField source="last_name" /> */}
      {/* <TextField source="preferred_name" /> */}
      {/* <DateField source="created_at" /> */}
      {/* <TextField source="home_phone" /> */}
      {/* <TextField source="work_phone" /> */}
      {/* <ReferenceField source="ishelters_id" reference="ishelters" /> */}
      {/* <NumberField source="created_by" /> */}
      {/* <NumberField source="address" /> */}
    </DatagridConfigurable>
  </List>
)
