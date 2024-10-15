import { TopToolbar, ExportButton, SelectColumnsButton } from 'react-admin';
import CustomExportButton from "../../components/CustomExportButton";


export const UserListActions = () => (
    <TopToolbar>
        <CreateButton /> {/* Create button should now appear */}
        <SelectColumnsButton />
        <ExportButton />
        {/* Custom Export to Excel Button */}
        <CustomExportButton /> {/* Add the CustomExportButton here */}
    </TopToolbar>
);
