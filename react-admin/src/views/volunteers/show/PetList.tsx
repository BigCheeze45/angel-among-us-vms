import {ENDPOINTS} from "../../../constants"
import {useList, Datagrid, DateField, TextField, Pagination, useRecordContext, ListContextProvider} from "react-admin"

export const EmptyPets = ({volunteerName}) => <div>No pets added yet for {volunteerName}</div>

export const PetList = () => {
  const record = useRecordContext()
  const data = record?.pets
  const listContext = useList({data})

  return (
    <ListContextProvider value={listContext}>
      <Datagrid
        resource={`${ENDPOINTS.VOLUNTEERS}/${record?.id}/pets`}
        rowClick={false}
        bulkActionButtons={false}
        empty={<EmptyPets volunteerName={record?.first_name} />}
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
