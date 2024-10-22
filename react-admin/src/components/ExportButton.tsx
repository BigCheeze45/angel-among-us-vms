import * as React from 'react';
import { useCallback } from 'react';
import DownloadIcon from '@mui/icons-material/GetApp';
import {
    fetchRelatedRecords,
    useDataProvider,
    useNotify,
    useListContext,
    Exporter,
} from 'ra-core';
import { Button, ButtonProps } from 'react-admin';

export const ExportButton = (props: ExportButtonProps) => {
    const {
        label = 'ra.action.export',
        icon = defaultIcon,
        meta,
        ...rest
    } = props;
    const {
        filter,
        filterValues,
        resource,
        sort,
        // exporter: exporterFromContext,
        total,
    } = useListContext();
    console.log("META =>", meta)
    // const exporter = customExporter || exporterFromContext;
    const dataProvider = useDataProvider();
    const notify = useNotify();
    const handleClick = useCallback(
        () => {
            console.log("I HAVE BEEN CLICKED")
            // dataProvider
            //     .getList(resource, {
            //         sort,
            //         filter: filter
            //             ? { ...filterValues, ...filter }
            //             : filterValues,
            //         pagination: { page: 1, perPage: maxResults },
            //         meta,
            //     })
            //     .then(
            //         ({ data }) =>
            //             exporter &&
            //             exporter(
            //                 data,
            //                 fetchRelatedRecords(dataProvider),
            //                 dataProvider,
            //                 resource
            //             )
            //     )
            //     .catch(error => {
            //         console.error(error);
            //         notify('ra.notification.http_error', { type: 'error' });
            //     });
            // if (typeof onClick === 'function') {
            //     onClick(event);
            // }
        },
        []
    );

    return (
        <Button
            onClick={handleClick}
            label={label}
            disabled={total === 0}
            {...sanitizeRestProps(rest)}
        >
            {icon}
        </Button>
    );
};

const defaultIcon = <DownloadIcon />;

const sanitizeRestProps = ({
    resource,
    ...rest
}: Omit<ExportButtonProps, 'maxResults' | 'label' | 'exporter' | 'meta'>) =>
    rest;

interface Props {
    // exporter?: Exporter;
    meta?: any
    label?: string
    icon?: JSX.Element
    // format?: string
    // maxResults?: number;
    // onClick?: (e: Event) => void;
    // resource?: string;
}

export type ExportButtonProps = Props & ButtonProps;
