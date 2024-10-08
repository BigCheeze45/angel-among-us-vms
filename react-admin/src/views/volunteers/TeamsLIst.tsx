import React from "react"
import {
    useList,
    Datagrid,
    TextField,
    useGetList,
    Pagination,
    CreateButton,
    useRecordContext,
    ListContextProvider,
} from "react-admin"
import { ENDPOINTS } from "../../constants"

const ActivitiesPagination = () => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />

export const VolunteerTeamsList = () => {
    const record = useRecordContext()
    const resource = `${ENDPOINTS.VOLUNTEERS}/${record?.id}/teams`
    const { data, isPending } = useGetList(
        resource,
        // TODO - add filtering and enhanced pagination
    )
    const listContext = useList({ data, isPending })

    return (
        <ListContextProvider value={listContext}>
            <CreateButton resource={resource} label="Add another team" />
            <Datagrid>
                <TextField source="team_name" label="Name" />
            </Datagrid>
            <ActivitiesPagination />
        </ListContextProvider>
    )
}
