import React, { useState } from 'react';
import {
    Dialog,
    DialogActions,
    DialogContent,
    DialogTitle,
    Button,
} from '@mui/material';
import { useNotify, useRefresh, SimpleForm, TextInput, useDataProvider, SelectInput } from 'react-admin';
import { Checkbox, FormControlLabel, } from '@mui/material';
import dataProvider from '../../dataProvider';
import { UserCreate } from './UserCreate';

interface CreateUserDialogProps {
    open: boolean;
    onClose: () => void;
}

const CreateUserDialog: React.FC<CreateUserDialogProps> = ({ open, onClose }) => {
    const notify = useNotify();
    const refresh = useRefresh();
    
    const [isStaff, setIsStaff] = useState<boolean>(false);
    const [isActive, setIsActive] = useState<boolean>(false);
    
    const handleIsStaffChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setIsStaff(event.target.checked);
    };

    const handleIsActiveChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setIsActive(event.target.checked);
    };
    const dataProvider = useDataProvider()
        
    const handleCreate = async () => {
        notify('User created successfully!');
        refresh();
        onClose();
    };

    return (
        <Dialog open={open} onClose={onClose}
        PaperProps={{
            style: {
                width: '400px',
                height: '660px',
                maxHeight:'none',
                maxWidth: 'none', 
            },
        }}
        >
            <DialogTitle>Create New User</DialogTitle>
            
            <DialogContent>
                <UserCreate/> 
            </DialogContent>
            <DialogActions>
                <Button onClick={onClose} color="primary">
                    Cancel
                </Button>
            </DialogActions>
        </Dialog>
    );
};

export default CreateUserDialog;
