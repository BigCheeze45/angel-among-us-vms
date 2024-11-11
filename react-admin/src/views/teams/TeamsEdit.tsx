import {
  Form,
  email,
  RaRecord,
  required,
  EditBase,
  maxLength,
  useNotify,
  useUpdate,
  TextInput,
  useRefresh,
  SaveButton,
} from "react-admin"
import {ENDPOINTS} from "../../constants"
import {Dialog, DialogTitle, DialogContent} from "@mui/material"

export const TeamEditDialog = (props: TeamEditDialogProps) => {
  const notify = useNotify()
  const refresh = useRefresh()
  const [update] = useUpdate()

  const {dialogOpen, onClose, record} = props

  const handleOnSubmit = values => {
    const payload = {
      id: values.id,
      email: values.email,
    }

    update(
      ENDPOINTS.TEAMS,
      {id: values.id, data: payload},
      {
        onSuccess: () => {
          onClose()
          refresh()
          notify("Team updated successfully", {type: "success"})
        },
        onError: error => {
          notify(`Failed to update team: ${error.message}`, {type: "error"})
        },
      },
    )
  }

  return (
    <Dialog
      open={dialogOpen}
      onClose={() => onClose()}
    >
      <DialogTitle>Edit {record?.name}</DialogTitle>
      <DialogContent>
        <EditBase
          id={record?.id}
          actions={false}
        >
          <Form onSubmit={handleOnSubmit}>
            <TextInput
              isRequired
              resettable
              source="email"
              validate={[required(), maxLength(100), email()]}
            />
            <SaveButton />
          </Form>
        </EditBase>
      </DialogContent>
    </Dialog>
  )
}

interface TeamEditDialogProps {
  dialogOpen: boolean
  onClose: () => void
  record: RaRecord | undefined | null
}
