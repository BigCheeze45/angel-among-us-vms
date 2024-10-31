import {
  List,
  TextField,
  TopToolbar,
  EmailField,
  FilterButton,
  FilterLiveSearch,
  SelectColumnsButton,
  DatagridConfigurable,
} from "react-admin"
import {Fragment} from "react"
import {ExportCSVButton} from "../../components/ExportCSVButton"
import {ExportExcelButton} from "../../components/ExportExcelButton"

const teamFilters = [
  <FilterLiveSearch
    key="teams_filter_livesearch"
    source="q"
    label="Search"
    placeholder="Search name, email or description"
    alwaysOn
  />,
]

const TeamsListActions = () => (
  <TopToolbar>
    <FilterButton />
    <ExportCSVButton />
    <ExportExcelButton />
    <SelectColumnsButton />
  </TopToolbar>
)
const TeamsBulkActionButtons = () => (
  <Fragment>
    <ExportCSVButton />
    <ExportExcelButton />
  </Fragment>
)

export const TeamList = () => (
  <List
    filters={teamFilters}
    actions={<TeamsListActions />}
  >
    <DatagridConfigurable bulkActionButtons={<TeamsBulkActionButtons />}>
      <TextField source="name" />
      <TextField source="description" />
      <EmailField source="email" />
      {/* <TextField source="id" /> */}
    </DatagridConfigurable>
  </List>
)
