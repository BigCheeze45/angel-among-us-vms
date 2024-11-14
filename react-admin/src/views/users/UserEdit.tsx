import {
  Form,
  choices,
  useNotify,
  useUpdate,
  TextInput,
  useRefresh,
  SaveButton,
  SelectInput,
  BooleanInput,
} from "react-admin"
import {ENDPOINTS} from "../../constants"
import {Dialog, DialogTitle, DialogContent} from "@mui/material"

export const UserEdit = props => {
  const notify = useNotify()
  const refresh = useRefresh()
  const [update] = useUpdate()

  const handleSubmit = formValues => {
    const {role} = formValues
    update(
      ENDPOINTS.USERS,
      {id: formValues.id, data: {...formValues, role: role.toLowerCase()}},
      {
        onSuccess: () => {
          refresh()
          props.onClose()
          notify(`${props.record.first_name} updated`, {type: "success"})
        },
        onError: error => {
          notify(`Failed to update record: ${error.message}`, {type: "error"})
        },
      },
    )
  }

  return (
    <Dialog
      open={props.dialogOpen}
      onClose={props.onClose}
    >
      <DialogTitle>Edit User</DialogTitle>
      <DialogContent>
        <Form
          record={props.record}
          onSubmit={handleSubmit}
        >
          <TextInput
            source="first_name"
            resettable
          />
          <div />
          <TextInput
            source="last_name"
            resettable
          />
          <div />
          <TextInput
            source="email"
            resettable
          />
          <div />
          <SelectInput
            resettable
            label="Role"
            source="role"
            create={false}
            choices={["Administrator", "Editor", "Viewer"]}
            validate={[choices(["Administrator", "Editor", "Viewer"], "Please choose one of the values")]}
          />
          <BooleanInput
            source="is_staff"
            helperText="Designates whether the user can log into this admin site."
          />
          <BooleanInput
            source="is_active"
            helperText="Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
          />
          <SaveButton sx={{mt: 1}} />
        </Form>
      </DialogContent>
    </Dialog>
  )
}
