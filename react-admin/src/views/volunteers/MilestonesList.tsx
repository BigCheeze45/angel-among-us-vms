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
    Pagination
} from "react-admin"
import { ENDPOINTS } from "../../constants"

const ActivitiesPagination = () => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />

export const VolunteerMilestonesList = () => {
    const record = useRecordContext()
    const resource = `${ENDPOINTS.VOLUNTEERS}/${record?.id}/milestones`
    const { data, isPending } = useGetList(
        resource,
        // { ids: [`${record.id}/activities`] }
    )
    const listContext = useList({ data, isPending })

    return (
        <ListContextProvider value={listContext}>
            <CreateButton resource={resource} label="Add new milestone" />
            <Datagrid>
                {/* <TextField source="id" /> */}
                <TextField source="award_title" label="Milestone" />
                <TextField source="achievement_level" label="Level" />
                <TextField source="award_description" label="Description" />
                <DateField source="milestone_date" label="Achieved on" />
            </Datagrid>
            <ActivitiesPagination />
        </ListContextProvider>
    )
}
