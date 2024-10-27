import {
  List,
  DateField,
  TextField,
  TopToolbar,
  FilterList,
  EditButton,
  EmailField,
  ExportButton,
  BooleanField,
  FilterButton,
  CreateButton,
  WrapperField,
  FilterListItem,
  BulkUpdateButton,
  SavedQueriesList,
  FilterLiveSearch,
  BulkExportButton,
  AutocompleteInput,
  SelectColumnsButton,
  DatagridConfigurable,
} from "react-admin";
import { Fragment, useState } from "react";
import { Card, CardContent, Button } from "@mui/material";
import StarBorderIcon from "@mui/icons-material/StarBorder";
import CardMembershipIcon from "@mui/icons-material/CardMembership";
import ExportExcelButton from "../../components/ExportExcelButton";
import CreateUserDialog from './CreateUserDialog';
import ContentAdd from '@mui/icons-material/Add';
import { ListActionToolbar } from "../../ListActionToolbar";

const UserListActions = ({ onCreateClick }: { onCreateClick: () => void; }) => (
  <TopToolbar>
      <FilterButton />
      <Button onClick={onCreateClick} startIcon={<ContentAdd />}>
           Create
      </Button>
      <ExportButton label="Export CSV" />
      <ExportExcelButton />
      <SelectColumnsButton />
  </TopToolbar>
);

const UsersBulkActionButtons = () => (
  <Fragment>
      <BulkUpdateButton label="Disable" data={{ is_active: false }} />
      <BulkExportButton label="Export CSV" />
      <ExportExcelButton />
  </Fragment>
);

const usersFilter = [
  <AutocompleteInput
      key="role_filter"
      source="group"
      label="Role"
      choices={["Administrator", "Viewer", "Editor"]}
  />,
];

const UsersFilterSidebar = () => (
  <Card sx={{ order: -1, mr: 2, mt: 6, mb: 7, width: 200 }}>
      <CardContent>
          <SavedQueriesList />
          <FilterLiveSearch
              source="q"
              label="Search"
              placeholder="Search name or email"
          />
          <FilterList label="Active" icon={<StarBorderIcon />}>
              <FilterListItem label="Yes" value={{ is_active: true }} />
              <FilterListItem label="No" value={{ is_active: false }} />
          </FilterList>
          <FilterList label="Superuser" icon={<CardMembershipIcon />}>
              <FilterListItem label="Yes" value={{ is_superuser: true }} />
              <FilterListItem label="No" value={{ is_superuser: false }} />
          </FilterList>
      </CardContent>
  </Card>
);

export const UsersList = () => {
  const [dialogOpen, setDialogOpen] = useState(false); 

  const handleCreateClick = () => {
      setDialogOpen(true);
  };

  const handleCloseDialog = () => {
      setDialogOpen(false); 
  };

  return (
      <>
          <List
              filters={usersFilter}
              actions={<UserListActions onCreateClick={handleCreateClick} />}
              aside={<UsersFilterSidebar />}
          >
              <DatagridConfigurable
                  omit={["Is staff"]}
                  bulkActionButtons={<UsersBulkActionButtons />}
              >
                  <WrapperField label="Name">
                      <TextField source="first_name" /> <TextField source="last_name" />
                  </WrapperField>
                  <EmailField source="email" />
                  <BooleanField source="is_active" />
                  <BooleanField source="is_superuser" />
                  <TextField source="last_login" />
                  <DateField source="date_joined" />
                  <WrapperField source="actions" label="">
                      <ListActionToolbar>
                          <EditButton />
                      </ListActionToolbar>
                  </WrapperField>
              </DatagridConfigurable>
          </List>
          <CreateUserDialog open={dialogOpen} onClose={handleCloseDialog} /> {/* Include the dialog */}
      </>
  );
};
