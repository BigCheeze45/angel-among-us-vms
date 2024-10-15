import {
  List,
  TextField,
  TopToolbar,
  EmailField,
  ExportButton,
  FilterButton,
  FilterLiveSearch,
  BulkExportButton,
  SelectColumnsButton,
  DatagridConfigurable,
} from "react-admin"
import {Fragment} from "react"
import ExportExcelButton from "../../components/ExportExcelButton"

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
    <ExportButton label="export csv" />
    <ExportExcelButton />
    <SelectColumnsButton />
  </TopToolbar>
)
const TeamsBulkActionButtons = () => (
  <Fragment>
    <BulkExportButton label="export csv" />
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
