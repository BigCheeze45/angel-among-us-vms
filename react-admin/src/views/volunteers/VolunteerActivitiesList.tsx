import {
  Form,
  useList,
  Datagrid,
  DateField,
  TextField,
  useCreate,
  useNotify,
  SaveButton,
  useRefresh,
  Pagination,
  TextInput,
  DateInput,
  useRecordContext,
  AutocompleteInput,
  ListContextProvider,
} from "react-admin"
import {useState} from "react"
import ContentAdd from "@mui/icons-material/Add"
import {ENDPOINTS, GA_COUNTIES} from "../../constants"
import {Dialog, DialogTitle, DialogContent, Button} from "@mui/material"

const ActivitiesPagination = () => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />
const EmptyActivities = () => <div>Volunteer has no activities yet</div>

export const VolunteerActivitiesList = () => {
  const [open, setOpen] = useState(false)
  const record = useRecordContext()
  const data = record?.activities
  const listContext = useList({data})

  const [create] = useCreate()
  const notify = useNotify()
  const refresh = useRefresh()

  const handleOpen = () => setOpen(true)
  const handleClose = () => setOpen(false)

  const handleCreate = async value => {
    console.log(value)
    const payload = {
      volunteer: value.id,
      location: value.location,
      start_date: value.start_date,
      activity_name: value.activity_name,
    }
    console.log(payload)
    const resource = `${ENDPOINTS.VOLUNTEERS}/${value.id}/activities`
    try {
      await create(resource, {data: payload})
      refresh()
      notify("Activity added successfully", {type: "success"})
      handleClose()
    } catch (error) {
      notify("Error adding activity", {type: "error"})
    }
  }

  const today = new Date().toISOString().split("T")[0] // Format: YYYY-MM-DD
  return (
    <ListContextProvider value={listContext}>
      <Button
        startIcon={<ContentAdd />}
        onClick={handleOpen}
        style={{marginBottom: "1rem"}}
      >
        Add new skill/interest
      </Button>
      <Datagrid
        rowClick={false}
        empty={<EmptyActivities />}
      >
        <TextField
          source="activity_name"
          label="Activity"
        />
        <TextField source="location" />
        <TextField source="description" />
        <DateField
          source="start_date"
          label="Date"
        />
      </Datagrid>
      <ActivitiesPagination />

      <Dialog
        open={open}
        onClose={handleClose}
        maxWidth="md"
      >
        <DialogTitle>New Activity</DialogTitle>
        <Form onSubmit={handleCreate}>
          <DialogContent>
            <TextInput
              source="activity_name"
              label="Activity"
              required
            />
            <TextInput source="description" />
            <DateInput
              source="start_date"
              defaultValue={today}
            />
            <AutocompleteInput
              isRequired
              source="location"
              choices={GA_COUNTIES}
            />
            <SaveButton />
          </DialogContent>
        </Form>
      </Dialog>
    </ListContextProvider>
  )
}
