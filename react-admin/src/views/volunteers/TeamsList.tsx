import {
    useList,
    Datagrid,
    TextField,
    useGetList,
    Pagination,
    CreateButton,
    useRecordContext,
    ListContextProvider,
    List,
} from "react-admin";
import { ENDPOINTS } from "../../constants";

import { TeamsListActions } from "./TeamsListActions";

const ActivitiesPagination = () => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} />;

export const VolunteerTeamsList = () => {
    const record = useRecordContext();
    const resource = `${ENDPOINTS.VOLUNTEERS}/${record?.id}/teams`;  

    
    const { data, isPending } = useGetList(
        resource,
        { pagination: { page: 1, perPage: 10 } }  
    );

    
    const listContext = useList({ data, isPending });

    return (
        <ListContextProvider value={listContext}>
            {/* Button to create a new team */}
            <CreateButton resource={resource} label="Add another team" />

            {/* Displaying the teams in a data grid */}
            <Datagrid>
                <TextField source="team_name" label="Team Name" />
            </Datagrid>
            <ActivitiesPagination />
        </ListContextProvider>
    );
};


export const TeamsList = () => (
    <List actions={<TeamsListActions />}>
        <Datagrid>
            <TextField source="team_name" label="Team Name" />
        </Datagrid>
    </List>
);
