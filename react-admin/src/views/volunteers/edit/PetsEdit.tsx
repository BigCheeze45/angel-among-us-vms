import {
  Form,
  useList,
  Datagrid,
  required,
  maxLength,
  TextField,
  useCreate,
  DateField,
  TextInput,
  useNotify,
  useUpdate,
  SaveButton,
  useRefresh,
  Pagination,
  useRecordContext,
  ListContextProvider,
  BulkDeleteWithConfirmButton,
} from "react-admin"
import {useState} from "react"
import {EmptyPets} from "../show/PetList"
import {ENDPOINTS} from "../../../constants"
import ContentAdd from "@mui/icons-material/Add"
import {Dialog, DialogTitle, DialogContent, Button} from "@mui/material"

const WrappedEmpty = ({volunteerName, hasPets}) => (hasPets ? null : <EmptyPets volunteerName={volunteerName} />)

export const PetsEdit = () => {
  const record = useRecordContext()
  const data = record?.pets
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
      const resource = `${ENDPOINTS.VOLUNTEERS}/${record?.id}/pets`

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
      volunteer: id,
      description: description,
    }

    const resource = `${ENDPOINTS.VOLUNTEERS}/${record?.id}/pets`
    create(
      resource,
      {data: payload},
      {
        onSuccess: () => {
          refresh()
          setDialogOpen(false)
          notify("Pet added successfully", {type: "success"})
        },
        onError: error => {
          notify(`Failed to add pet: ${error.message}`, {type: "error"})
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
        Add new Pet
      </Button>
      <Datagrid
        sx={{width: 1}}
        resource={`${ENDPOINTS.VOLUNTEERS}/${record?.id}/pets`}
        bulkActionButtons={
          <BulkDeleteWithConfirmButton
            mutationMode="optimistic"
            confirmTitle="Delete pets"
            confirmColor="warning"
            onClick={refresh}
          />
        }
        rowClick={(_id, _resource, row) => {
          setEditing(true)
          setSelectedRow(row)
          setDialogOpen(!dialogOpen)
          return false
        }}
        empty={
          <WrappedEmpty
            hasPets={data.length === 0}
            volunteerName={record?.first_name}
          />
        }
      >
        <TextField source="description" />
        <DateField
          source="updated_at"
          label="Updated"
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
      >
        <DialogTitle>{editing ? "Edit Pet" : "New Pet"}</DialogTitle>
        {editing ? (
          <DialogContent>
            <Form
              onSubmit={handleSave}
              record={selectedRow}
            >
              <TextInput
                multiline
                isRequired
                source="description"
                validate={[required(), maxLength(500)]}
              />
              <SaveButton />
            </Form>
          </DialogContent>
        ) : (
          <DialogContent>
            <Form onSubmit={handleSave}>
              <TextInput
                multiline
                isRequired
                source="description"
                validate={[required(), maxLength(500)]}
              />
              <SaveButton />
            </Form>
          </DialogContent>
        )}
      </Dialog>
    </ListContextProvider>
  )
}
