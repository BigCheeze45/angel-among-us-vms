import {
  Form,
  useList,
  Datagrid,
  useCreate,
  useNotify,
  TextField,
  useRefresh,
  Pagination,
  SaveButton,
  useRecordContext,
  AutocompleteInput,
  ListContextProvider,
} from "react-admin"
import {useState} from "react"
import {ENDPOINTS} from "../../constants"
import ContentAdd from "@mui/icons-material/Add"
import {Dialog, DialogTitle, DialogContent, Button} from "@mui/material"
import { resourceUsage } from "process"

const ActivitiesPagination = () => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />
const EmptySkills = () => <div>Volunteer has no skills/interests yet</div>
const skillOptions = [
  {id: "Fundraising", name: "Fundraising"},
  {id: "Photography", name: "Photography"},
  {id: "Transportation", name: "Transportation"},
  {id: "Graphic Design", name: "Graphic Design"},
  {id: "Creative Writing", name: "Creative Writing"},
  {id: "Helping at Events", name: "Helping at Events"},
  {id: "Administrative Work", name: "Administrative Work"},
  {id: "Education and Community", name: "Education and Community"},
]

export const VolunteerSkillsList = () => {
  const [open, setOpen] = useState(false)
  const record = useRecordContext()
  const data = record?.skills
  const listContext = useList({data})

  const [create] = useCreate()
  const notify = useNotify()
  const refresh = useRefresh()

  const handleOpen = () => setOpen(true)
  const handleClose = () => setOpen(false)

  const handleCreate = async ({id, skill}) => {

    const resource = `${ENDPOINTS.VOLUNTEERS}/${id}/skills`
    try {
      await create(resource, {data: {volunteer: id, skill}})
      refresh()
      notify("Skill added successfully", {type: "success"})
      handleClose()
    } catch (error) {
      notify("Error adding skill", {type: "error"})
    }
  }

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
        empty={<EmptySkills />}
      >
        <TextField source="skill" />
        {/* <DeleteButton onClick={} redirect={false}/> */}
      </Datagrid>
      <ActivitiesPagination />

      <Dialog
        open={open}
        onClose={handleClose}
        maxWidth="md"
      >
        <DialogTitle>New Skill/Interest</DialogTitle>
        <Form onSubmit={handleCreate}>
          <DialogContent>
            <AutocompleteInput
              isRequired
              source="skill"
              choices={skillOptions}
              onCreate={newSkill => {
                const newOption = {id: newSkill?.toLowerCase(), name: newSkill}
                skillOptions.push(newOption)
                return newOption
              }}
            />
            <SaveButton />
          </DialogContent>
        </Form>
      </Dialog>
    </ListContextProvider>
  )
}
