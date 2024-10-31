import {
  Form,
  List,
  email,
  choices,
  useNotify,
  DateField,
  TextInput,
  useCreate,
  TextField,
  TopToolbar,
  FilterList,
  EditButton,
  EmailField,
  SaveButton,
  SelectInput,
  useRedirect,
  ExportButton,
  BooleanField,
  FilterButton,
  CreateButton,
  WrapperField,
  FilterListItem,
  BulkUpdateButton,
  SavedQueriesList,
  FilterLiveSearch,
  BulkExportButton,
  AutocompleteInput,
  CheckboxGroupInput,
  SelectColumnsButton,
  DatagridConfigurable,
} from "react-admin"
import {Fragment, useState} from "react"
import {ENDPOINTS} from "../../constants"
import {ListActionToolbar} from "../../ListActionToolbar"
import StarBorderIcon from "@mui/icons-material/StarBorder"
import CardMembershipIcon from "@mui/icons-material/CardMembership"
import ExportExcelButton from "../../components/ExportExcelButton"
import {Card, CardContent, Dialog, DialogTitle, DialogContent} from "@mui/material"

const UserListActions = ({onCreateClick}) => (
  <TopToolbar>
    <FilterButton />
    <CreateButton
      onClick={e => {
        e.preventDefault()
        onCreateClick()
      }}
    />
    <ExportButton label="Export CSV" />
    <ExportExcelButton />
    <SelectColumnsButton />
  </TopToolbar>
)

const UsersBulkActionButtons = () => (
  <Fragment>
    <BulkUpdateButton
      label="Disable"
      data={{is_active: false}}
    />
    <BulkExportButton label="Export CSV" />
    <ExportExcelButton />
  </Fragment>
)

const usersFilter = [
  <AutocompleteInput
    key="role_filter"
    source="group"
    label="Role"
    choices={["Administrator", "Viewer", "Editor"]}
  />,
]

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

export const UsersList = () => {
  const notify = useNotify()
  const [create] = useCreate()
  const validateEmail = email()
  const redirect = useRedirect()
  const [dialogOpen, setDialogOpen] = useState(false)
  const validateRole = choices(["administrator", "editor", "viewer"], "Please choose one of the values")

  const handleCreate = formValues => {
    const {is_staff, ...rest} = formValues
    const payload = {...rest, is_staff: is_staff.length === 1}
    create(
      ENDPOINTS.USERS,
      {data: payload},
      {
        onSuccess: data => {
          // console.log(data)
          setDialogOpen(!dialogOpen)
          notify(`Added ${data.first_name} ${data.last_name}`, {type: "success"})
          redirect("show", ENDPOINTS.USERS, data.id)
        },
        onError: error => {
          // console.log("ERROR")
          // console.log(error)
          notify(error.message, {type: "error"})
        },
      },
    )
  }

  return (
    <>
      <List
        filters={usersFilter}
        actions={<UserListActions onCreateClick={() => setDialogOpen(true)} />}
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
          <DateField
            source="last_login"
            showTime
          />
          <DateField source="date_joined" />
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

      {/* region create dialog */}
      <Dialog
        open={dialogOpen}
        onClose={() => setDialogOpen(!dialogOpen)}
      >
        <DialogTitle>Add New User</DialogTitle>
        <DialogContent>
          <Form onSubmit={handleCreate}>
            <TextInput
              source="first_name"
              label="First Name"
              required={true}
            />
            <TextInput
              source="last_name"
              label="Last Name"
              required={true}
            />
            <TextInput
              source="email"
              label="Email"
              validate={validateEmail}
              required={true}
            />
            <SelectInput
              source="role"
              label="Role"
              required={true}
              validate={validateRole}
              defaultValue="viewer"
              choices={[
                {id: "administrator", name: "Administrator"},
                {id: "viewer", name: "Viewer"},
                {id: "editor", name: "Editor"},
              ]}
            />
            <CheckboxGroupInput
              label={false}
              source="is_staff"
              choices={["Staff"]}
              defaultValue={["Staff"]}
              options={{required: true}}
              helperText="Designates whether the user can log into the VMS"
            />
            <SaveButton
              label="Create user"
              sx={{mt: 1}}
            />
          </Form>
        </DialogContent>
      </Dialog>
      {/* endregion */}
    </>
  )
}
