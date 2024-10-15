import { TopToolbar, ExportButton, SelectColumnsButton } from 'react-admin';
import CustomExportButton from "../../components/CustomExportButton";


export const TeamsListActions = () => (
    <TopToolbar>
        <SelectColumnsButton />
        <ExportButton />
        {/* Custom Export to Excel Button */}
        <CustomExportButton /> {/* Add the CustomExportButton here */}
    </TopToolbar>
);
