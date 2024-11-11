import {
  Form,
  choices,
  required,
  useList,
  Datagrid,
  maxLength,
  useCreate,
  useNotify,
  TextField,
  useRefresh,
  Pagination,
  SaveButton,
  useRecordContext,
  AutocompleteInput,
  ListContextProvider,
  RadioButtonGroupInput,
  BulkDeleteWithConfirmButton,
} from "react-admin"
import {useState} from "react"
import {ENDPOINTS, VOLUNTEER_SKILLS} from "../../../constants"
import ContentAdd from "@mui/icons-material/Add"
import {Dialog, DialogTitle, DialogContent, Button} from "@mui/material"
import {EmptySkills} from "../SkillsList"

const ActivitiesPagination = () => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />

const WrappedEmpty = ({volunteerName, hasSkills}) => (hasSkills ? null : <EmptySkills volunteerName={volunteerName} />)

export const SkillsEdit = () => {
  const record = useRecordContext()
  const data = record?.skills
  const listContext = useList({data})
  const [dialogOpen, setDialogOpen] = useState(false)

  const notify = useNotify()
  const refresh = useRefresh()
  const [create] = useCreate()

  const handleCreate = ({id, skill}) => {
    const resource = `${ENDPOINTS.VOLUNTEERS}/${id}/skills`
    create(
      resource,
      {data: {volunteer: id, skill}},
      {
        onSuccess: () => {
          refresh()
          setDialogOpen(false)
          notify("Skill added successfully", {type: "success"})
        },
        onError: error => {
          notify(`Failed to add skill: ${error.message}`, {type: "error"})
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
        Add new skill/interest
      </Button>
      <Datagrid
        resource={`${ENDPOINTS.VOLUNTEERS}/${record?.id}/skills`}
        sx={{width: 1}}
        bulkActionButtons={
          <BulkDeleteWithConfirmButton
            mutationMode="optimistic"
            confirmTitle="Delete skill/interest"
            confirmColor="warning"
            onClick={refresh}
          />
        }
        rowClick={false}
        empty={
          <WrappedEmpty
            hasSkills={data.length === 0}
            volunteerName={record?.first_name}
          />
        }
      >
        <TextField source="skill" />
      </Datagrid>
      <ActivitiesPagination />

      <Dialog
        open={dialogOpen}
        onClose={() => setDialogOpen(!dialogOpen)}
        fullWidth
        maxWidth="xs"
      >
        <DialogTitle>New Skill/Interest</DialogTitle>
        <DialogContent>
          <Form onSubmit={handleCreate}>
            <AutocompleteInput
              isRequired
              label="Options"
              source="skill"
              choices={VOLUNTEER_SKILLS}
              onCreate={newSkill => {
                const newOption = {id: newSkill?.toLowerCase(), name: newSkill}
                VOLUNTEER_SKILLS.push(newOption)
                return newOption
              }}
              validate={[required(), maxLength(100)]}
            />
            <RadioButtonGroupInput
              isRequired
              label="Type"
              source="category"
              choices={[
                {id: "skill", name: "Skill"},
                {id: "interest", name: "Interest"},
              ]}
              validate={[
                required("Please choose one of the values"),
                choices(["skill", "interest", "Please choose one of the values"]),
              ]}
            />
            <SaveButton />
          </Form>
        </DialogContent>
      </Dialog>
    </ListContextProvider>
  )
}
