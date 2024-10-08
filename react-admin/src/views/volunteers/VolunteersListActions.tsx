import {
    TopToolbar,
    ExportButton,
    SelectColumnsButton,
} from "react-admin"

export const VolunteersListActions = () => (
    <TopToolbar>
        <SelectColumnsButton />
        <ExportButton />
    </TopToolbar>
)
