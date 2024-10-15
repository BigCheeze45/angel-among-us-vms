import {
    List,
    TextField,
    EmailField,
    BooleanField,
    DateField,
    DatagridConfigurable
} from "react-admin"

import { VolunteersListActions } from "./VolunteersListActions"
import { VolunteerFilterSidebar } from "./VolunteersFilterSidebar"
import { VolunteerBulkActionButtons } from "./VolunteerBulkActionButtons"

export const VolunteersList = () => (
    <List actions={<VolunteersListActions />} aside={<VolunteerFilterSidebar />}>
        <DatagridConfigurable bulkActionButtons={<VolunteerBulkActionButtons />}>
            <TextField source="full_name" label="Name" />
            <EmailField source="email" />
            <DateField source="date_joined" />
            <DateField source="active_status_change_date" />
            <BooleanField source="active" />
            <TextField source="cell_phone" />
            <DateField source="date_of_birth" />
            <TextField source="ishelters_category_type" />
            <BooleanField source="ishelters_access_flag" />
            <DateField source="maddie_certifications_received_date" />
            {/* <TextField source="id" /> */}
            {/* <TextField source="first_name" /> */}
            {/* <TextField source="middle_name" /> */}
            {/* <TextField source="last_name" /> */}
            {/* <TextField source="preferred_name" /> */}
            {/* <DateField source="created_at" /> */}
            {/* <TextField source="home_phone" /> */}
            {/* <TextField source="work_phone" /> */}
            {/* <ReferenceField source="ishelters_id" reference="ishelters" /> */}
            {/* <NumberField source="created_by" /> */}
            {/* <NumberField source="address" /> */}
        </DatagridConfigurable>
    </List>
)
