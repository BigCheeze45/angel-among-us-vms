import { TopToolbar, ExportButton, SelectColumnsButton } from 'react-admin';
import ExportExcelButton from "../../components/CustomExportButton";


export const UserListActions = () => (
    <TopToolbar>
        <CreateButton /> {/* Create button should now appear */}
        <SelectColumnsButton />
        <ExportButton />
        {/* Custom Export to Excel Button */}
        <ExportExcelButton /> {/* Add the CustomExportButton here */}
    </TopToolbar>
);
