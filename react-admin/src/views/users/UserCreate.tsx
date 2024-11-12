import {
  Form,
  email,
  choices,
  required,
  TextInput,
  useCreate,
  useNotify,
  useRefresh,
  SaveButton,
  SelectInput,
  CheckboxGroupInput,
} from "react-admin"
import {useCallback} from "react"
import {ENDPOINTS} from "../../constants"
import {Dialog, DialogTitle, DialogContent} from "@mui/material"

export const UserCreate = (props: UserCreateDialogProps) => {
  const {dialogOpen, onClose} = props
  const notify = useNotify()
  const refresh = useRefresh()
  const [create] = useCreate()

  const handleCallback = useCallback(() => {
    onClose()
  }, [onClose])

  const handleCreate = formValues => {
    const {is_staff, ...rest} = formValues
    const payload = {...rest, is_staff: is_staff.length === 1}
    create(
      ENDPOINTS.USERS,
      {data: payload},
      {
        onSuccess: data => {
          handleCallback()
          refresh()
          notify(`Added ${data.first_name}`, {type: "success"})
        },
        onError: error => {
          notify(`Fail to add user: ${error.message}`, {type: "error"})
        },
      },
    )
  }

  return (
    <Dialog
      open={dialogOpen}
      onClose={handleCallback}
    >
      <DialogTitle>Add New User</DialogTitle>
      <DialogContent>
        <Form onSubmit={handleCreate}>
          <TextInput
            isRequired
            validate={[required()]}
            source="first_name"
          />
          <div />
          <TextInput
            source="last_name"
            required={true}
          />
          <div />
          <TextInput
            isRequired
            source="email"
            validate={[required(), email()]}
          />
          <div />
          <SelectInput
            isRequired
            source="role"
            defaultValue="viewer"
            choices={[
              {id: "administrator", name: "Administrator"},
              {id: "viewer", name: "Viewer"},
              {id: "editor", name: "Editor"},
            ]}
            validate={[required(), choices(["administrator", "editor", "viewer"], "Please choose one of the values")]}
          />
          <div />
          <CheckboxGroupInput
            label={false}
            source="is_staff"
            choices={["Staff"]}
            defaultValue={["Staff"]}
            // options={{required: true}}
            helperText="Designates whether the user can log into the VMS"
          />
          <div />
          <SaveButton
            label="Create user"
            sx={{mt: 1}}
          />
        </Form>
      </DialogContent>
    </Dialog>
  )
}

interface UserCreateDialogProps {
  dialogOpen: boolean
  onClose: () => void
}
