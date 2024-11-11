import {ENDPOINTS} from "../../../constants"
import {useList, Datagrid, DateField, TextField, Pagination, useRecordContext, ListContextProvider} from "react-admin"

const EmptyChildren = ({volunteerName}) => <div>No Children added yet for {volunteerName}</div>

export const ChildrenList = () => {
  const record = useRecordContext()
  const data = record?.children
  const listContext = useList({data})

  return (
    <ListContextProvider value={listContext}>
      <Datagrid
        rowClick={false}
        bulkActionButtons={false}
        resource={`${ENDPOINTS.VOLUNTEERS}/${record?.id}/children`}
        empty={<EmptyChildren volunteerName={record?.first_name} />}
      >
        <TextField source="description" />
        <DateField
          source="updated_at"
          label="Updated"
        />
      </Datagrid>
      <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />
    </ListContextProvider>
  )
}
