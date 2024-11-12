import {
  List,
  DateField,
  TextField,
  TopToolbar,
  FilterList,
  EmailField,
  CreateButton,
  BooleanField,
  WrapperField,
  FilterListItem,
  BulkUpdateButton,
  SavedQueriesList,
  FilterLiveSearch,
  SelectColumnsButton,
  DatagridConfigurable,
} from "react-admin"
import {UserEdit} from "./UserEdit"
import {UserCreate} from "./UserCreate"
import {Fragment, useState} from "react"
import {Card, CardContent} from "@mui/material"
import BadgeIcon from '@mui/icons-material/Badge'
import VisibilityIcon from '@mui/icons-material/Visibility'
import StarBorderIcon from "@mui/icons-material/StarBorder"
import {ExportCSVButton} from "../../components/ExportCSVButton"
import {ExportExcelButton} from "../../components/ExportExcelButton"

const UserListActions = (props: UserListActionsProps) => (
  <TopToolbar>
    <CreateButton
      onClick={e => {
        e.preventDefault()
        e.stopPropagation()
        props.onCreateClick()
      }}
    />
    <ExportCSVButton />
    <ExportExcelButton />
    <SelectColumnsButton />
  </TopToolbar>
)

const UsersBulkActionButtons = () => (
  <Fragment>
    <BulkUpdateButton
      label="Disable"
      mutationMode="optimistic"
      successMessage="Logins disabled successfully"
      data={{is_active: false, is_staff: false, disable: true}}
    />
    <ExportCSVButton />
    <ExportExcelButton />
  </Fragment>
)

const UsersFilterSidebar = () => (
  <Card sx={{order: -1, mr: 2, mt: 6, mb: 7, width: 200}}>
    <CardContent>
      <SavedQueriesList />
      <FilterLiveSearch
        source="q"
        label="Search"
        placeholder="Search name or email"
      />
      <FilterList
        label="Active"
        icon={<StarBorderIcon />}
      >
        <FilterListItem
          label="Yes"
          value={{is_active: true}}
        />
        <FilterListItem
          label="No"
          value={{is_active: false}}
        />
      </FilterList>
      <FilterList
        label="VMS Access"
        icon={<VisibilityIcon />}
      >
        <FilterListItem
          label="Yes"
          value={{is_staff: true}}
        />
        <FilterListItem
          label="No"
          value={{is_staff: false}}
        />
      </FilterList>
      <FilterList
        label="Role"
        icon={<BadgeIcon />}
      >
        <FilterListItem
          label="Administrator"
          value={{role: "administrator"}}
        />
        <FilterListItem
          label="Editor"
          value={{role: "editor"}}
        />
        <FilterListItem
          label="Viewer"
          value={{role: "viewer"}}
        />
      </FilterList>
    </CardContent>
  </Card>
)

export const UsersList = () => {
  const [dialogOpen, setDialogOpen] = useState(false)
  const [selectedRow, setSelectedRow] = useState(undefined)
  const [editing, setEditing] = useState(false)

  return (
    <>
      <List
        actions={<UserListActions onCreateClick={() => setDialogOpen(!dialogOpen)} />}
        aside={<UsersFilterSidebar />}
      >
        <DatagridConfigurable
          bulkActionButtons={<UsersBulkActionButtons />}
          rowClick={(_id, _resource, record) => {
            setSelectedRow(record)
            setEditing(!editing)
            return false
          }}
        >
          <WrapperField label="Name">
            <TextField source="first_name" /> <TextField source="last_name" />
          </WrapperField>
          <EmailField source="email" />
          <BooleanField
            source="is_active"
            label="Active"
          />
          <BooleanField
            source="is_staff"
            label="VMS Access"
          />
          <DateField
            showTime
            label="Last Login"
            source="last_login"
          />
          <DateField
            label="Date Joined"
            source="date_joined"
          />
        </DatagridConfigurable>
      </List>
      <UserCreate
        dialogOpen={dialogOpen}
        onClose={() => setDialogOpen(!dialogOpen)}
      />
      <UserEdit
        dialogOpen={editing}
        onClose={() => setEditing(!editing)}
        record={selectedRow}
      />
    </>
  )
}

interface UserListActionsProps {
  onCreateClick: () => void
}
