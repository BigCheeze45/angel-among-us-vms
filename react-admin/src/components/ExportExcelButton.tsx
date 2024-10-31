import {ExportButton} from "./ExportButton"

export const ExportExcelButton = (meta, {...rest}) => (
  <ExportButton
    label="export excel"
    meta={{format: "excel", ...meta}}
    {...rest}
  />
)
