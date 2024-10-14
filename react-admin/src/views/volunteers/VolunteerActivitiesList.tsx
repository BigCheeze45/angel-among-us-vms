import React from "react"
import {
  List,
  Admin,
  Resource,
  EditGuesser,
  ShowGuesser,
  ListGuesser,
  Datagrid,
  BooleanField,
  DateField,
  useRecordContext,
  useGetList,
  NumberField,
  useList,
  EmailField,
  ListContextProvider,
  CreateButton,
  TextField,
  Pagination,
} from "react-admin"
import {ENDPOINTS} from "../../constants"

const ActivitiesPagination = () => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />

export const VolunteerActivitiesList = () => {
  const record = useRecordContext()
  const resource = `${ENDPOINTS.VOLUNTEERS}/${record?.id}/activities`
  const {data, isPending} = useGetList(
    resource,
    // { ids: [`${record.id}/activities`] }
  )
  const listContext = useList({data, isPending})

  return (
    <ListContextProvider value={listContext}>
      <CreateButton
        resource={resource}
        label="Add new activity"
      />
      <Datagrid>
        <TextField
          source="activity_name"
          label="Activity"
        />
        {/* <TextField source="id" /> */}
        <TextField source="location" />
        <TextField source="status" />
        <DateField source="start_date" />
        <DateField source="end_date" />
        <TextField source="description" />
        <NumberField
          source="hours_spent"
          label="Duration"
        />
        {/* <TextField source="name" /> */}
      </Datagrid>
      <ActivitiesPagination />
    </ListContextProvider>
  )
}
