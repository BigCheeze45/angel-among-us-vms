import { TopToolbar, ExportButton, SelectColumnsButton } from 'react-admin';
import ExportExcelButton from "../../components/ExportExcelButton";


export const VolunteersListActions = () => (
    <TopToolbar>
        <ExportButton />
        <ExportExcelButton />
        <SelectColumnsButton />
    </TopToolbar>
);
