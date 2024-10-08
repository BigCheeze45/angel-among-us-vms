import {
    BulkDeleteButton,
    BulkExportButton,
    BulkUpdateButton,
} from "react-admin"
import React from "react"
import { Fragment } from "react"

export const VolunteerBulkActionButtons = () => (
    <Fragment>
        <BulkExportButton />
        {/* <BulkUpdateButton data={{ active: false }} /> */}
        {/* <BulkDeleteButton /> */}
    </Fragment>
)
