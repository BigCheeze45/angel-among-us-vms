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
  const [dialogOpen, setDialogOpen] = useState(false)
  const record = useRecordContext()
  const data = record?.pets
  const listContext = useList({data})

  const notify = useNotify()
  const [create] = useCreate()
  const refresh = useRefresh()

  const handleCreate = ({id, description}) => {
    const payload = {
      volunteer: id,
      description: description,
    }

    const resource = `${ENDPOINTS.VOLUNTEERS}/${id}/pets`
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
        onClick={() => setDialogOpen(!dialogOpen)}
        style={{marginBottom: "1rem"}}
      >
        Add new Pet
      </Button>
      <Datagrid
        sx={{width: 1}}
        rowClick={false}
        resource={`${ENDPOINTS.VOLUNTEERS}/${record?.id}/pets`}
        bulkActionButtons={
          <BulkDeleteWithConfirmButton
            mutationMode="optimistic"
            confirmTitle="Delete pets"
            confirmColor="warning"
            onClick={refresh}
          />
        }
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
        onClose={() => setDialogOpen(!dialogOpen)}
        maxWidth="md"
        fullWidth
      >
        <DialogTitle>New Pet</DialogTitle>
        <DialogContent>
          <Form onSubmit={handleCreate}>
            <TextInput
              multiline
              isRequired
              source="description"
              validate={[required(), maxLength(500)]}
            />
            <SaveButton />
          </Form>
        </DialogContent>
      </Dialog>
    </ListContextProvider>
  )
}
