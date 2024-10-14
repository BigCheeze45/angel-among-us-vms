import {
  List,
  DateField,
  TextField,
  TopToolbar,
  FilterList,
  EditButton,
  EmailField,
  ExportButton,
  BooleanField,
  FilterButton,
  WrapperField,
  FilterListItem,
  BulkUpdateButton,
  SavedQueriesList,
  FilterLiveSearch,
  BulkExportButton,
  AutocompleteInput,
  SelectColumnsButton,
  DatagridConfigurable,
} from "react-admin"
import {Fragment} from "react"
import {Card, CardContent} from "@mui/material"
import StarBorderIcon from "@mui/icons-material/StarBorder"
import {ListActionToolbar} from "../../ListActionToolbar"
import CardMembershipIcon from "@mui/icons-material/CardMembership"

const UserListActions = () => (
  <TopToolbar>
    <FilterButton />
    <ExportButton label="export csv" />
    <SelectColumnsButton />
  </TopToolbar>
)

const UsersBulkActionButtons = () => (
  <Fragment>
    <BulkUpdateButton
      label="disable"
      data={{is_active: false}}
    />
    <BulkExportButton label="export csv" />
  </Fragment>
)

const usersFilter = [
  <AutocompleteInput
    key="role_filter"
    source="group"
    label="Role"
    choices={["Administrator", "Manager", "Editor"]}
  />,
]

const UsersFilterSidebar = () => {
  return (
    <Card sx={{order: -1, mr: 2, mt: 6, mb: 7, width: 200}}>
      <CardContent>
        <SavedQueriesList />
        <FilterLiveSearch
          source="q"
          label="Search"
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
          label="Superuser"
          icon={<CardMembershipIcon />}
        >
          <FilterListItem
            label="Yes"
            value={{is_superuser: true}}
          />
          <FilterListItem
            label="No"
            value={{is_superuser: false}}
          />
        </FilterList>
      </CardContent>
    </Card>
  )
}

export const UsersList = () => (
  <List
    filters={usersFilter}
    actions={<UserListActions />}
    aside={<UsersFilterSidebar />}
  >
    <DatagridConfigurable
      omit={["Is staff"]}
      bulkActionButtons={<UsersBulkActionButtons />}
    >
      <TextField source="first_name" />
      <TextField source="last_name" />
      <EmailField source="email" />
      <BooleanField source="is_active" />
      <BooleanField source="is_superuser" />
      <TextField source="last_login" />
      <DateField source="date_joined" />
      {/* https://marmelab.com/react-admin/SelectColumnsButton.html#adding-a-label-to-unlabeled-columns */}
      <WrapperField
        source="actions"
        label=""
      >
        <ListActionToolbar>
          <EditButton />
        </ListActionToolbar>
      </WrapperField>
      {/* <TextField source="username" /> */}
      {/* <BooleanField source="is_staff" /> */}
      {/* <DateField source="password" /> */}
      {/* <TextField source="id" /> */}
      {/* <TextField source="groups" /> */}
      {/* <TextField source="user_permissions" /> */}
    </DatagridConfigurable>
  </List>
)
