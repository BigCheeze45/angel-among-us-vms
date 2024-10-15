import {
    List,
    TextField,
    EmailField,
    BooleanField,
    DateField,
    Datagrid,
    TopToolbar,
    CreateButton,
    ExportButton,
    SelectColumnsButton
} from "react-admin";
import CustomExportButton from "../../components/CustomExportButton";  

export const UserListActions = () => (
    <TopToolbar>
        <CreateButton /> {/* Create button for creating a new user */}
        <SelectColumnsButton /> {/* Allow the user to select visible columns */}
        <ExportButton /> {/* Default export functionality */}
        <CustomExportButton /> {/* Custom export to Excel button */}
    </TopToolbar>
);

export const UserList = () => (
    <List actions={<UserListActions />}> {/* Add UserListActions in List toolbar */}
        <Datagrid> {/* Display the data in a table grid */}
            <TextField source="first_name" />
            <TextField source="last_name" />
            <TextField source="username" />
            <EmailField source="email" />
            <BooleanField source="is_superuser" />
            <BooleanField source="is_staff" />
            <BooleanField source="is_active" />
            <TextField source="last_login" />
            <DateField source="date_joined" />
            {/* Optional fields (commented out) */}
            {/* <DateField source="password" /> */}
            {/* <TextField source="id" /> */}
            {/* <TextField source="groups" /> */}
            {/* <TextField source="user_permissions" /> */}
        </Datagrid>
    </List>
);
