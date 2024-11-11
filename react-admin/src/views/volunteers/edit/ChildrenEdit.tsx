import {
  Form,
  useList,
  Datagrid,
  required,
  maxLength,
  DateField,
  TextField,
  TextInput,
  useCreate,
  useNotify,
  SaveButton,
  useRefresh,
  Pagination,
  EditButton,
  WrapperField,
  useRecordContext,
  ListContextProvider,
  BulkDeleteWithConfirmButton,
} from "react-admin"
import {useState} from "react"
import {ENDPOINTS} from "../../../constants"
import ContentAdd from "@mui/icons-material/Add"
import {ListActionToolbar} from "../../../components/ListActionToolbar"
import {Dialog, DialogTitle, DialogContent, Button} from "@mui/material"

const EmptyChildren = ({volunteerName}) => <div>No children added yet for {volunteerName}</div>
const WrappedEmpty = ({volunteerName, hasChildren}) =>
  hasChildren ? null : <EmptyChildren volunteerName={volunteerName} />

export const ChildrenEdit = () => {
  const record = useRecordContext()
  const data = record?.children
  const listContext = useList({data})
  const [editing, setEditing] = useState(false)
  const [dialogOpen, setDialogOpen] = useState(false)

  const notify = useNotify()
  const [create] = useCreate()
  const refresh = useRefresh()

  const handleCreate = ({id, description}) => {
    const payload = {
      volunteer: id,
      description: description,
    }

    const resource = `${ENDPOINTS.VOLUNTEERS}/${id}/children`
    create(
      resource,
      {data: payload},
      {
        onSuccess: () => {
          refresh()
          setDialogOpen(false)
          notify("Child added successfully", {type: "success"})
        },
        onError: error => {
          notify(`Failed to add child: ${error.message}`, {type: "error"})
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
        Add new child
      </Button>
      <Datagrid
        sx={{width: 1}}
        rowClick={false}
        resource={`${ENDPOINTS.VOLUNTEERS}/${record?.id}/children`}
        bulkActionButtons={
          <BulkDeleteWithConfirmButton
            mutationMode="optimistic"
            confirmTitle="Delete children"
            confirmColor="warning"
            onClick={refresh}
          />
        }
        empty={
          <WrappedEmpty
            volunteerName={record?.first_name}
            hasChildren={data.length === 0}
          />
        }
      >
        <TextField source="description" />
        <DateField
          source="updated_at"
          label="Updated"
        />
        {/* <WrapperField
          source="actions"
          label=""
        >
          <ListActionToolbar>
            <EditButton
              onClick={e => {
                e.preventDefault()
                console.log("EDITING")
                setEditing(!editing)
              }}
            />
          </ListActionToolbar>
        </WrapperField> */}
      </Datagrid>
      <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />

      <Dialog
        open={dialogOpen}
        onClose={() => setDialogOpen(!dialogOpen)}
        // maxWidth="md"
        fullWidth
      >
        <DialogTitle>New child</DialogTitle>
        <DialogContent>
          <Form onSubmit={handleCreate}>
            <TextInput
              isRequired
              multiline
              source="description"
              validate={[required(), maxLength(500)]}
            />
            <SaveButton />
          </Form>
        </DialogContent>
      </Dialog>

      {/* <Dialog
        open={editing}
        onClose={() => setEditing(!editing)}
        maxWidth="md"
        fullWidth
      >
        <DialogTitle>Edit child</DialogTitle>
        <DialogContent>
          <Form onSubmit={() => console.log("SUBMITTING EDIT")}>
            <TextInput
              isRequired
              multiline
              source="description"
              validate={[required(), maxLength(500)]}
            />
            <SaveButton />
          </Form>
        </DialogContent>
      </Dialog> */}
    </ListContextProvider>
  )
}
