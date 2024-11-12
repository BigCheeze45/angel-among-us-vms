import {Dialog, DialogTitle, DialogContent} from "@mui/material"
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

export const UserEdit = props => {
  const notify = useNotify()
  const refresh = useRefresh()
  const [update] = useUpdate()

  const handleSubmit = formValues => {
    // console.log(formValues)
    // // const {groups, roles, user_permissions, id, ...rest} = formValues
    // // console.log(rest)
    // // return
    update(
      ENDPOINTS.USERS,
      {id: formValues.id, data: {...formValues}},
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
          <TextInput
            source="last_name"
            resettable
          />
          <TextInput
            source="email"
            resettable
          />
          <SelectInput
            resettable
            label="Role"
            source="role"
            validate={[choices(["administrator", "editor", "viewer"], "Please choose one of the values")]}
            choices={[
              {id: "administrator", name: "Administrator"},
              {id: "viewer", name: "Viewer"},
              {id: "editor", name: "Editor"},
            ]}
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
