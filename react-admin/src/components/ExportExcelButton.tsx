import { Button } from '@mui/material';
import { useListContext } from 'react-admin';
import DownloadIcon from '@mui/icons-material/GetApp';
import { exportToExcel } from '../components/exportToExcel';

const ExportExcelButton: React.FC = () => {
    const { data } = useListContext();

    const handleExcelExport = () => {
        if (data && data.length > 0) {
            exportToExcel(data, 'volunteers_export.xlsx');
        }
    };

    {/* Custom Excel export button */}
    return (
            <div>
                <Button onClick={handleExcelExport} startIcon={<DownloadIcon />}>
                    Export Excel
                </Button>
            </div>
    );
};

export default ExportExcelButton;
