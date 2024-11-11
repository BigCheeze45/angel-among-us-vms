import {
  List,
  DateField,
  TextField,
  ChipField,
  TopToolbar,
  FilterList,
  EditButton,
  EmailField,
  ArrayField,
  CreateButton,
  BooleanField,
  WrapperField,
  FilterListItem,
  SingleFieldList,
  BulkUpdateButton,
  SavedQueriesList,
  FilterLiveSearch,
  SelectColumnsButton,
  DatagridConfigurable,
} from "react-admin"
import {UserCreate} from "./UserCreate"
import {Fragment, useState} from "react"
import {Card, CardContent} from "@mui/material"
import StarBorderIcon from "@mui/icons-material/StarBorder"
import {ExportCSVButton} from "../../components/ExportCSVButton"
import {ListActionToolbar} from "../../components/ListActionToolbar"
import CardMembershipIcon from "@mui/icons-material/CardMembership"
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
      data={{is_active: false, is_staff: false}}
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
        icon={<CardMembershipIcon />}
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
        icon={<CardMembershipIcon />}
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

  return (
    <>
      <List
        actions={<UserListActions onCreateClick={() => setDialogOpen(!dialogOpen)} />}
        aside={<UsersFilterSidebar />}
      >
        <DatagridConfigurable bulkActionButtons={<UsersBulkActionButtons />}>
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
          {/* <ArrayField
            source="roles"
            label="Role"
            sortable={false}
          >
            <SingleFieldList linkType={false}>
              <ChipField
                source="name"
                size="small"
              />
            </SingleFieldList>
          </ArrayField> */}
          <DateField
            showTime
            label="Last Login"
            source="last_login"
          />
          <DateField
            label="Date Joined"
            source="date_joined"
          />
          <WrapperField
            source="actions"
            label=""
          >
            <ListActionToolbar>
              <EditButton />
            </ListActionToolbar>
          </WrapperField>
        </DatagridConfigurable>
      </List>
      <UserCreate
        dialogOpen={dialogOpen}
        onClose={() => setDialogOpen(!dialogOpen)}
      />
    </>
  )
}

interface UserListActionsProps {
  onCreateClick: () => void
}
