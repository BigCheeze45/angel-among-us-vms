import {
  List,
  TextField,
  TopToolbar,
  EmailField,
  ShowButton,
  WrapperField,
  FilterLiveSearch,
  SavedQueriesList,
  SelectColumnsButton,
  DatagridConfigurable,
} from "react-admin"
import {Fragment, useState} from "react"
import {TeamEditDialog} from "./TeamsEdit"
import {Card, CardContent} from "@mui/material"
import {ExportCSVButton} from "../../components/ExportCSVButton"
import {ExportExcelButton} from "../../components/ExportExcelButton"
import {ListActionToolbar} from "../../components/ListActionToolbar"

export const TeamFilterSidebar = () => {
  return (
    // -1 display on the left rather than on the right of the list
    <Card sx={{order: -1, mr: 2, mt: 6, mb: 7, width: 200}}>
      <CardContent>
        <SavedQueriesList />
        <FilterLiveSearch
          source="q"
          label="Search"
        />
      </CardContent>
    </Card>
  )
}

const TeamsListActions = () => (
  <TopToolbar>
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

export const TeamList = () => {
  const [dialogOpen, setDialogOpen] = useState(false)
  const [selectedRecord, setSelectedRecord] = useState(undefined)

  return (
    <List
      actions={<TeamsListActions />}
      aside={<TeamFilterSidebar />}
    >
      <DatagridConfigurable
        bulkActionButtons={<TeamsBulkActionButtons />}
        rowClick={(_id, _resource, record) => {
          setSelectedRecord(record)
          setDialogOpen(!dialogOpen)
          return false
        }}
      >
        <TextField source="name" />
        <TextField source="description" />
        <EmailField source="email" />
        <WrapperField
          source="actions"
          label=""
        >
          <ListActionToolbar>
            <ShowButton label="View team" />
          </ListActionToolbar>
        </WrapperField>
      </DatagridConfigurable>
      <TeamEditDialog
        record={selectedRecord}
        dialogOpen={dialogOpen}
        onClose={() => setDialogOpen(!dialogOpen)}
      />
    </List>
  )
}
