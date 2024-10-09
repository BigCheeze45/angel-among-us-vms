import { BooleanInput, DateInput, Create, NumberInput, ReferenceInput, SimpleForm, TextInput } from 'react-admin';

export const VolunteersCreate = () => (
    <Create>
        <SimpleForm>
            <TextInput source="id" />
            <TextInput source="first_name" />
            <TextInput source="middle_name" />
            <TextInput source="last_name" />
            <TextInput source="preferred_name" />
            <TextInput source="full_name" />
            <TextInput source="email" />
            <DateInput source="date_joined" />
            <DateInput source="active_status_change_date" />
            <DateInput source="created_at" />
            <BooleanInput source="active" />
            <TextInput source="cell_phone" />
            <TextInput source="home_phone" />
            <TextInput source="work_phone" />
            <DateInput source="date_of_birth" />
            <TextInput source="ishelters_category_type" />
            <BooleanInput source="ishelters_access_flag" />
            <ReferenceInput source="ishelters_id" reference="ishelters" />
            <DateInput source="maddie_certifications_received_date" />
            <NumberInput source="created_by" />
            <NumberInput source="address" />
        </SimpleForm>
    </Create>
);