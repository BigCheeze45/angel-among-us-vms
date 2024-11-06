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
  import {Dialog, DialogTitle, DialogContent, Button, alertTitleClasses} from "@mui/material"
  
  const ActivitiesPagination = () => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />
  const EmptyActivities = () => <div>No Children added yet</div>
  
  export const ChildrenList = () => {
    const [open, setOpen] = useState(false)
    const record = useRecordContext()
    const data = record?.children

    const listContext = useList({data})
  
    const [create] = useCreate()
    const notify = useNotify()
    const refresh = useRefresh()
  
    const handleOpen = () => setOpen(true)
    const handleClose = () => setOpen(false)
  
    const handleCreate = async ({id,description}) => {

      const payload = {
        volunteer: id,
        description: description,
      }

      const resource = `${ENDPOINTS.VOLUNTEERS}/${id}/children`;
      console.log(resource,'rsssss')
      const dd={data: payload};
      console.log(dd,'dd')
      try {
        await create(resource, {data: payload})
        refresh()
        notify("Children added successfully", {type: "success"})
        handleClose()
      } catch (error) {
        notify("Error adding Children", {type: "error"})
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
          Add new Children
        </Button>
        <Datagrid
          rowClick={false}
          empty={<EmptyActivities />}
        >
          <TextField
          source="description"
          label="Description"
        />

        <DateField
        source="created_at"
        label="Date Created"
      />
        <DateField
        source="updated_at"
        label="Date Updated"
      />
        </Datagrid>
        <ActivitiesPagination />
  
        <Dialog
          open={open}
          onClose={handleClose}
          maxWidth="md"
        >
          <DialogTitle>New Children</DialogTitle>
          <Form onSubmit={handleCreate}>
            <DialogContent>
              <TextInput
            source="description"
            label="Description"
                required
              />
              {/* <DateInput
                source="created_at"
                defaultValue={today}
              />
                  <DateInput
                source="updated_at"
                defaultValue={today}
              /> */}
            
              <SaveButton />
            </DialogContent>
          </Form>
        </Dialog>
      </ListContextProvider>
    )
  }
  