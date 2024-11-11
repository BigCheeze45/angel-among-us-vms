import {ENDPOINTS} from "../../../constants"
import {useList, Datagrid, DateField, TextField, Pagination, useRecordContext, ListContextProvider} from "react-admin"

export const EmptyActivities = ({volunteerName}) => <div>{volunteerName} has no activities yet</div>

export const ActivitiesList = () => {
  const record = useRecordContext()
  const data = record?.activities
  const listContext = useList({data})

  return (
    <ListContextProvider value={listContext}>
      <Datagrid
        rowClick={false}
        bulkActionButtons={false}
        resource={`${ENDPOINTS.VOLUNTEERS}/${record?.id}/activities`}
        empty={<EmptyActivities volunteerName={record?.first_name} />}
      >
        <TextField
          source="activity_name"
          label="Activity"
        />
        {/* <TextField source="location" /> */}
        <TextField source="description" />
        <DateField
          source="start_date"
          label="Date"
        />
      </Datagrid>
      <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />
    </ListContextProvider>
  )
}
