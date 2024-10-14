import {TopToolbar, ExportButton, FilterButton, SelectColumnsButton} from "react-admin"

export const VolunteersListActions = () => (
  <TopToolbar>
    <FilterButton />
    <ExportButton label="export csv" />
    <SelectColumnsButton />
  </TopToolbar>
)
