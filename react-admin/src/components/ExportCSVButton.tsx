import {ExportButton} from "./ExportButton"

export const ExportCSVButton = (meta, {...rest}) => (
  <ExportButton
    label="export csv"
    meta={{format: "csv", ...meta}}
    {...rest}
  />
)
