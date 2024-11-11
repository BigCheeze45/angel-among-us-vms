import {
  Form,
  useList,
  required,
  Datagrid,
  maxLength,
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
  ListContextProvider,
  BulkDeleteWithConfirmButton,
} from "react-admin"
import {useState} from "react"
import {ENDPOINTS} from "../../../constants"
import {format, startOfToday} from "date-fns"
import ContentAdd from "@mui/icons-material/Add"
import {EmptyActivities} from "../show/VolunteerActivitiesList"
import {Dialog, DialogTitle, DialogContent, Button} from "@mui/material"

const WrappedEmpty = ({volunteerName, hasActivities}) =>
  hasActivities ? null : <EmptyActivities volunteerName={volunteerName} />

export const ActivitiesEdit = () => {
  const record = useRecordContext()
  const data = record?.activities
  const listContext = useList({data})
  const [dialogOpen, setDialogOpen] = useState(false)

  const [create] = useCreate()
  const notify = useNotify()
  const refresh = useRefresh()

  const createNewActivity = formValues => {
    const payload = {
      volunteer: formValues.id,
      location: formValues.location,
      description: formValues.description,
      activity_name: formValues.activity_name,
      start_date: format(formValues.start_date, "yyyy-MM-dd"),
    }

    const resource = `${ENDPOINTS.VOLUNTEERS}/${formValues.id}/activities`
    create(
      resource,
      {data: payload},
      {
        onSuccess: () => {
          refresh()
          setDialogOpen(false)
          notify("Activity added successfully", {type: "success"})
        },
        onError: error => {
          notify(`Failed to add activity: ${error.message}`, {type: "error"})
        },
      },
    )
  }

  return (
    <ListContextProvider value={listContext}>
      <Button
        startIcon={<ContentAdd />}
        onClick={() => setDialogOpen(!dialogOpen)}
        style={{marginBottom: "1rem"}}
      >
        Add new Activity
      </Button>
      <Datagrid
        resource={`${ENDPOINTS.VOLUNTEERS}/${record?.id}/activities`}
        bulkActionButtons={
          <BulkDeleteWithConfirmButton
            confirmTitle="Delete activities"
            mutationMode="optimistic"
            confirmColor="warning"
            onClick={refresh}
          />
        }
        sx={{width: 1}}
        rowClick={false}
        empty={
          <WrappedEmpty
            volunteerName={record?.first_name}
            hasActivities={record?.activities === 0}
          />
        }
      >
        <TextField
          source="activity_name"
          label="Activity"
        />
        <TextField source="description" />
        <DateField
          source="start_date"
          label="Date"
        />
      </Datagrid>
      <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />

      <Dialog
        open={dialogOpen}
        onClose={() => setDialogOpen(!dialogOpen)}
        // maxWidth="md"
      >
        <DialogTitle>New Activity</DialogTitle>
        <DialogContent>
          <Form onSubmit={createNewActivity}>
            <TextInput
              isRequired
              validate={[required(), maxLength(200)]}
              resettable
              source="activity_name"
              label="Activity"
            />
            <TextInput
              resettable
              multiline
              source="description"
              validate={maxLength(500)}
            />
            <DateInput
              isRequired
              validate={required()}
              source="start_date"
              defaultValue={startOfToday()}
            />
            {/* <AutocompleteInput
              isRequired
              source="location"
              choices={GA_COUNTIES}
            /> */}
            <SaveButton />
          </Form>
        </DialogContent>
      </Dialog>
    </ListContextProvider>
  )
}
