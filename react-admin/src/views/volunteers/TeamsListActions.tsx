import { TopToolbar, ExportButton, SelectColumnsButton } from 'react-admin';
import ExportExcelButton from "../../components/CustomExportButton";


export const TeamsListActions = () => (
    <TopToolbar>
        <SelectColumnsButton />
        <ExportButton />
        {/* Custom Export to Excel Button */}
        <ExportExcelButton /> {/* Add the CustomExportButton here */}
    </TopToolbar>
);
