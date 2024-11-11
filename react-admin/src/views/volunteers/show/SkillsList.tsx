import {ENDPOINTS} from "../../../constants"
import {useList, Datagrid, TextField, Pagination, useRecordContext, ListContextProvider} from "react-admin"

const ActivitiesPagination = () => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />
export const EmptySkills = ({volunteerName}) => <div>{volunteerName} has no skills/interests yet</div>

export const VolunteerSkillsList = () => {
  const record = useRecordContext()
  const data = record?.skills
  const listContext = useList({data})

  return (
    <ListContextProvider value={listContext}>
      <Datagrid
        resource={`${ENDPOINTS.VOLUNTEERS}/${record?.id}/skills`}
        bulkActionButtons={false}
        rowClick={false}
        empty={<EmptySkills volunteerName={record?.first_name} />}
      >
        <TextField source="skill" />
        <TextField source="type" />
      </Datagrid>
      <ActivitiesPagination />
    </ListContextProvider>
  )
}
