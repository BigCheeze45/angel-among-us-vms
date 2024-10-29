import {Fragment} from "react"
import {BulkExportButton} from "react-admin"

export const VolunteerBulkActionButtons = () => (
  <Fragment>
    <BulkExportButton label="export csv" />
    {/* <BulkUpdateButton data={{ active: false }} /> */}
    {/* <BulkDeleteButton /> */}
  </Fragment>
)
