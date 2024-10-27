import { useState } from 'react';
import { Create, SimpleForm, SelectInput, TextInput } from "react-admin";
import { Checkbox, FormControlLabel } from '@mui/material';

export const UserCreate = () => {
  
  const [isStaff, setIsStaff] = useState<boolean>(false);
  const [isActive, setIsActive] = useState<boolean>(false);

  
  const handleIsStaffChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setIsStaff(event.target.checked);
  };

  const handleIsActiveChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setIsActive(event.target.checked);
  };

  return (
    <Create>
      <SimpleForm>
        <TextInput
          source="first_name"
          label="First Name"
          required={true}
        />
        <TextInput
          source="last_name"
          label="Last Name"
          required={true}
        />
        <TextInput
          source="email"
          label="Email"
          required={true}
        />
        <SelectInput
          source="role"
          label="Role"
          required={true}
          choices={[
            { id: 'administrator', name: 'Administrator' },
            { id: 'viewer', name: 'Viewer' },
            { id: 'editor', name: 'Editor' },
          ]}
        />
      
        <FormControlLabel
          control={
            <Checkbox
              checked={isStaff}
              onChange={handleIsStaffChange}
            />
          }
          label="Staff"
        />
        
        <FormControlLabel
          control={
            <Checkbox
              checked={isActive}
              onChange={handleIsActiveChange}
            />
          }
          label="Active"
        />
      </SimpleForm>
    </Create>
  );
};

