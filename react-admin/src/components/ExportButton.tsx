import {useCallback} from "react"
import {saveAs} from "file-saver"
import {Button, ButtonProps} from "react-admin"
import DownloadIcon from "@mui/icons-material/GetApp"
import {useNotify, useListContext, useDataProvider} from "ra-core"

export const ExportButton = (props: ExportButtonProps) => {
  const {label = "ra.action.export", icon = defaultIcon, meta, ...rest} = props

  const {sort, total, filter, resource, filterValues, selectedIds} = useListContext()

  const dataProvider = useDataProvider()
  const notify = useNotify()
  const handleClick = useCallback(() => {
    dataProvider
      .export(resource, {
        sort,
        filter: filter ? {...filterValues, ...filter} : filterValues,
        meta,
        ids: selectedIds,
      })
      .then(data => {
        const filename = `${resource}.${meta?.format === "csv" ? "csv" : "xlsx"}`
        saveAs(data, filename)
      })
      .catch(error => {
        console.log(error)
        // pop up a generic error
        notify("ra.notification.http_error", {type: "error"})
      })
  }, [dataProvider, filter, filterValues, meta, notify, resource, selectedIds, sort])

  return (
    <Button
      onClick={handleClick}
      label={label}
      disabled={total === 0}
      {...sanitizeRestProps(rest)}
    >
      {icon}
    </Button>
  )
}

const defaultIcon = <DownloadIcon />

const sanitizeRestProps = ({
  resource,
  ...rest
}: Omit<ExportButtonProps, "maxResults" | "label" | "exporter" | "meta">) => rest

interface Props {
  meta?: any
  label?: string
  resource?: string
  icon?: JSX.Element
}

export type ExportButtonProps = Props & ButtonProps
