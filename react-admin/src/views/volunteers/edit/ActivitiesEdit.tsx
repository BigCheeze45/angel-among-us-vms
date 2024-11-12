import {
  Form,
  useList,
  required,
  Datagrid,
  TextInput,
  DateInput,
  maxLength,
  DateField,
  TextField,
  useUpdate,
  useCreate,
  useNotify,
  SaveButton,
  useRefresh,
  Pagination,
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
  const [editing, setEditing] = useState(false)
  const [dialogOpen, setDialogOpen] = useState(false)
  const [selectedRow, setSelectedRow] = useState(undefined)

  const notify = useNotify()
  const [create] = useCreate()
  const [update] = useUpdate()
  const refresh = useRefresh()

  const handleSave = formValues => {
    if (editing) {
      const resource = `${ENDPOINTS.VOLUNTEERS}/${record?.id}/activities`

      update(
        resource,
        {id: selectedRow?.id, data: {...formValues}},
        {
          onSuccess: () => {
            setEditing(false)
            refresh()
            setDialogOpen(!dialogOpen)
            notify("Record updated successfully", {type: "success"})
          },
          onError: error => {
            notify(`Failed to update record: ${error.message}`, {type: "error"})
          },
        },
      )
      return
    }

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
        onClick={() => {
          setEditing(false)
          setDialogOpen(!dialogOpen)
        }}
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
        rowClick={(_id, _resource, row) => {
          setEditing(true)
          setSelectedRow(row)
          setDialogOpen(!dialogOpen)
          return false
        }}
        empty={
          <WrappedEmpty
            volunteerName={record?.first_name}
            hasActivities={record?.activities.length === 0}
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
        onClose={() => {
          setEditing(false)
          setSelectedRow(undefined)
          setDialogOpen(!dialogOpen)
        }}
        // maxWidth="md"
      >
        <DialogTitle>{editing ? "Edit Activity" : "New Activity"}</DialogTitle>
        {editing ? (
          <DialogContent>
            <Form
              onSubmit={handleSave}
              record={selectedRow}
            >
              <TextInput
                isRequired
                resettable
                label="Activity"
                source="activity_name"
                validate={[required(), maxLength(200)]}
              />
              <div />
              <TextInput
                resettable
                multiline
                source="description"
                validate={maxLength(500)}
              />
              <div />
              <DateInput
                isRequired
                source="start_date"
                validate={required()}
                defaultValue={startOfToday()}
              />
              <div />
              <SaveButton />
            </Form>
          </DialogContent>
        ) : (
          <DialogContent>
            <Form onSubmit={handleSave}>
              <TextInput
                isRequired
                resettable
                label="Activity"
                source="activity_name"
                validate={[required(), maxLength(200)]}
              />
              <div />
              <TextInput
                resettable
                multiline
                source="description"
                validate={maxLength(500)}
              />
              <div />
              <DateInput
                isRequired
                source="start_date"
                validate={required()}
                defaultValue={startOfToday()}
              />
              <div />
              <SaveButton />
            </Form>
          </DialogContent>
        )}
      </Dialog>
    </ListContextProvider>
  )
}
