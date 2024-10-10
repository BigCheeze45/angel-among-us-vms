// eslint-disable-next-line @typescript-eslint/no-unused-vars
import React from "react"

import {
    List,
    TextField,
    EmailField,
    BooleanField,
    DateField,
    Datagrid,
} from "react-admin"


export const UserList = () => (
    <List>
        <Datagrid>
            <TextField source="first_name" />
            <TextField source="last_name" />
            <TextField source="username" />
            <EmailField source="email" />
            <BooleanField source="is_superuser" />
            <BooleanField source="is_staff" />
            <BooleanField source="is_active" />
            <TextField source="last_login" />
            <DateField source="date_joined" />
            {/* <DateField source="password" /> */}
            {/* <TextField source="id" /> */}
            {/* <TextField source="groups" /> */}
            {/* <TextField source="user_permissions" /> */}
        </Datagrid>
    </List>
)
