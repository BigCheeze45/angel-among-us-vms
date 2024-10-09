import React from 'react';
import { TopToolbar, useListContext, ExportButton } from 'react-admin';
import { Button } from '@mui/material';
import { exportToExcel } from './exportToExcel';

const CustomExportButton: React.FC = () => {
    const { data } = useListContext();

    const handleExcelExport = () => {
        if (data && data.length > 0) {
            exportToExcel(data, 'exported_data.xlsx'); // Modify filename if needed
        }
    };

    return (
        <TopToolbar>
            {/* Default JSON export button */}
            <ExportButton />
            {/* Custom Excel export button */}
            <Button onClick={handleExcelExport} variant="contained" color="primary">
                Export to Excel
            </Button>
        </TopToolbar>
    );
};

export default CustomExportButton;
