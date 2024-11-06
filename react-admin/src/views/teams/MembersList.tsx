import {
  useList,
  Datagrid,
  DateField,
  TextField,
  Pagination,
  EmailField,
  ShowButton,
  useRecordContext,
  ListContextProvider,
} from "react-admin"
import {ENDPOINTS} from "../../constants"
import {ListActionToolbar} from "../../components/ListActionToolbar"

const EmptyMembers = () => <div>Team has no members yet</div>
const ActivitiesPagination = () => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />

export const TeamMembersList = () => {
  const record = useRecordContext()
  const data = record?.members
  const listContext = useList({data})

  return (
    <ListContextProvider value={listContext}>
      <Datagrid
        empty={<EmptyMembers />}
        bulkActionButtons={false}
        // disable row clicking, instead click view volunteer to go to volunteer SHOW page
        rowClick={false}
      >
        <TextField
          source="full_name"
          label="Name"
        />
        <EmailField source="email" />
        <DateField source="start_date" />
        <DateField source="end_date" />
        <ListActionToolbar>
          <ShowButton
            label="view volunteer"
            resource={`${ENDPOINTS.VOLUNTEERS}`}
          />
        </ListActionToolbar>
      </Datagrid>
      <ActivitiesPagination />
    </ListContextProvider>
  )
}
