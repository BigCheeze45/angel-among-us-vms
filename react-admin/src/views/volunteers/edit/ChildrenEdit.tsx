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
  useUpdate,
  Pagination,
  useRecordContext,
  ListContextProvider,
  BulkDeleteWithConfirmButton,
} from "react-admin"
import {useState} from "react"
import {ENDPOINTS} from "../../../constants"
import ContentAdd from "@mui/icons-material/Add"
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
  const [selectedRow, setSelectedRow] = useState(undefined)

  const notify = useNotify()
  const [create] = useCreate()
  const [update] = useUpdate()
  const refresh = useRefresh()

  const handleSave = ({id, description}) => {
    if (editing) {
      const resource = `${ENDPOINTS.VOLUNTEERS}/${record?.id}/children`
      update(
        resource,
        {id, data: {description}},
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

    const resource = `${ENDPOINTS.VOLUNTEERS}/${id}/children`
    create(
      resource,
      {data: {volunteer: id, description: description}},
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
        onClick={() => {
          setEditing(false)
          setDialogOpen(!dialogOpen)
        }}
        style={{marginBottom: "1rem"}}
      >
        Add new child
      </Button>
      <Datagrid
        sx={{width: 1}}
        rowClick={(_id, _resource, row) => {
          setEditing(true)
          setSelectedRow(row)
          setDialogOpen(!dialogOpen)
          return false // do nothing
        }}
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
        // fullWidth
      >
        <DialogTitle>{editing ? "Edit child" : "New child"}</DialogTitle>
        {editing ? (
          // #region Edit dialog
          <>
            <DialogContent>
              <Form
                onSubmit={handleSave}
                record={selectedRow}
              >
                <TextInput
                  isRequired
                  multiline
                  source="description"
                  validate={[required(), maxLength(500)]}
                />
                <div />
                <SaveButton />
              </Form>
            </DialogContent>
          </>
        ) : (
          // #endregion
          // #region Create dialog
          <>
            <DialogContent>
              <Form onSubmit={handleSave}>
                <TextInput
                  isRequired
                  multiline
                  source="description"
                  validate={[required(), maxLength(500)]}
                />
                <div />
                <SaveButton />
              </Form>
            </DialogContent>
          </>
          //#endregion
        )}
      </Dialog>
    </ListContextProvider>
  )
}
