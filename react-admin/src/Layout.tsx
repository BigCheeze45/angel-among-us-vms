import type { ReactNode } from "react";
import { Layout as RALayout, AppBar, CheckForApplicationUpdate } from "react-admin";
import IconButton from '@mui/material/IconButton';
import Brightness4Icon from '@mui/icons-material/Brightness4';
import Brightness7Icon from '@mui/icons-material/Brightness7';
import Typography from '@mui/material/Typography';
import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import { Box } from "@mui/material";
import CustomMenu from './CustomMenu';

const CustomAppBar = ({ toggleTheme, isDarkMode }) => {
    const location = useLocation();
    const [pageTitle, setPageTitle] = useState('');
    const [selectedPerson, setSelectedPerson] = useState('');

    useEffect(() => {
        if (location.pathname === '/volunteers' || location.pathname === '/volunteers/create') {
            setPageTitle('Volunteers');
        } else if (location.pathname === '/teams' || location.pathname === '/teams/create') {
            setPageTitle('Teams');
        } else if (location.pathname === '/users' || location.pathname === '/users/create') {
            setPageTitle('Users');
        }
        if (location.pathname.includes('/volunteers/')) {
            setPageTitle('Volunteer');
            setSelectedPerson('Name'); // Replace with actual name logic
        } else if (location.pathname.includes('/teams/')) {
            setPageTitle('Team');
            setSelectedPerson('Team Name'); // Replace with actual team name logic
        } else if (location.pathname.includes('/users/')) {
            setPageTitle('User');
            setSelectedPerson('Name'); // Replace with actual user name logic
        } else {
            setSelectedPerson(''); // Reset if not on a detail page
        }
    }, [location.pathname]);

    return (
        <AppBar>
            <Box sx={{ display: 'flex', alignItems: 'center', width: '82%' }}>
                <Typography variant="h6" style={{ marginLeft: 16 }}>
                    {pageTitle} {selectedPerson && `- ${selectedPerson}`}
                </Typography>

                <IconButton
                    onClick={toggleTheme}
                    style={{ marginLeft: 'auto', marginRight: 16 }}
                    color="inherit"
                    aria-label={isDarkMode ? 'Switch to light mode' : 'Switch to dark mode'}
                >
                    {isDarkMode ? <Brightness7Icon /> : <Brightness4Icon />}
                </IconButton>
            </Box>
        </AppBar>
    );
};

export const Layout = ({ children, toggleTheme, isDarkMode }: { children: ReactNode; toggleTheme: () => void; isDarkMode: boolean }) => (
    <RALayout
        appBar={(appBarProps) => (
            <CustomAppBar
                {...appBarProps}
                toggleTheme={toggleTheme}
                isDarkMode={isDarkMode}
            />
        )}
        menu={() => <CustomMenu width="300px" />}
    >
        <Box sx={{ marginLeft: -1}}> 
            {children}
        </Box>
        <CheckForApplicationUpdate />
    </RALayout>
);

export default Layout;

