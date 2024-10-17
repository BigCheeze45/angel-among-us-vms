import {
  useList,
  Datagrid,
  RaRecord,
  DateField,
  TextField,
  Pagination,
  ShowButton,
  useRecordContext,
  ListContextProvider,
} from "react-admin"
import {ENDPOINTS} from "../../constants"
import {ListActionToolbar} from "../../ListActionToolbar"

const ActivitiesPagination = () => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />
const EmptyTeams = (record: RaRecord) => <div>{`${record.full_name}`} is not on any team</div>

export const VolunteerTeamsList = () => {
  const record = useRecordContext()
  const data = record?.teams
  const listContext = useList({data})

  return (
    <ListContextProvider value={listContext}>
      <Datagrid
        rowClick={false}
        empty={<EmptyTeams />}
        bulkActionButtons={false}
      >
        <TextField source="name" />
        <DateField source="start_date" />
        <DateField source="end_date" />
        <ListActionToolbar>
          <ShowButton
            label="view team"
            resource={`${ENDPOINTS.TEAMS}`}
          />
        </ListActionToolbar>
      </Datagrid>
      <ActivitiesPagination />
    </ListContextProvider>
  )
}
