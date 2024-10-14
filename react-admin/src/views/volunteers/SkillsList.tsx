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

export const VolunteerSkillsList = () => {
  const record = useRecordContext()
  const resource = `${ENDPOINTS.VOLUNTEERS}/${record?.id}/skills`
  const {data, isPending} = useGetList(
    resource,
    // { ids: [`${record.id}/activities`] }
  )
  const listContext = useList({data, isPending})

  return (
    <ListContextProvider value={listContext}>
      <CreateButton
        resource={resource}
        label="Add new skill"
      />
      <Datagrid>
        {/* <TextField source="id" /> */}
        <TextField source="description" />
        <NumberField source="proficiency_level" />
        <NumberField source="years_of_experience" />
      </Datagrid>
      <ActivitiesPagination />
    </ListContextProvider>
  )
}
