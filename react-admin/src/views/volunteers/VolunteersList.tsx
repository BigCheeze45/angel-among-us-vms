import {
  List,
  UrlField,
  DateField,
  TextField,
  TopToolbar,
  EmailField,
  FilterButton,
  BooleanField,
  ReferenceInput,
  AutocompleteInput,
  SelectColumnsButton,
  DatagridConfigurable,
} from "react-admin"
import {Fragment} from "react"
import {GA_COUNTIES, VOLUNTEER_SKILLS} from "../../constants"
import {ExportCSVButton} from "../../components/ExportCSVButton"
import {VolunteerFilterSidebar} from "./VolunteersFilterSidebar"
import {ExportExcelButton} from "../../components/ExportExcelButton"

const volunteerFilters = [
  <AutocompleteInput
    key="skill_filter"
    source="skill"
    choices={VOLUNTEER_SKILLS}
  />,
  <ReferenceInput
    key="team_filter"
    source="team_id"
    reference="teams"
    perPage={25}
    sx={{width: 1}}
    sort={{field: "name", order: "ASC"}}
  />,
  <AutocompleteInput
    key="county_filter"
    source="county"
    choices={GA_COUNTIES}
  />,
  <AutocompleteInput
    key="interest_filter"
    source="interest"
    choices={VOLUNTEER_SKILLS}
  />,
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

export const VolunteersList = () => {
  return (
    <List
      filters={volunteerFilters}
      actions={<VolunteersListActions />}
      aside={<VolunteerFilterSidebar />}
    >
      <DatagridConfigurable
        bulkActionButtons={<VolunteerBulkActionButtons />}
        omit={["work_phone", "home_phone", "date_of_birth", "maddie_certifications_received_date", "ishelters_profile"]}
      >
        <TextField
          source="full_name"
          label="Name"
        />
        <TextField source="preferred_name" />
        <EmailField source="email" />
        <DateField source="date_joined" />
        <BooleanField source="active" />
        <TextField source="cell_phone" />
        <DateField
          source="date_of_birth"
          label="Birth date"
        />
        <TextField source="job_title" />
        <DateField
          source="application_received_date"
          showTime
          label="Last updated"
        />
        <DateField
          source="maddie_certifications_received_date"
          label="Maddie certification date"
        />
        <TextField source="home_phone" />
        <TextField source="work_phone" />
        <UrlField
          target="_blank"
          rel="noopener noreferrer"
          source="ishelters_profile"
          label="iShelters Profile"
          content="View iShelters profile"
        />
      </DatagridConfigurable>
    </List>
  )
}
