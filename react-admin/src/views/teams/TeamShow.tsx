import {
  BooleanField,
  DateField,
  EmailField,
  ReferenceField,
  SimpleShowLayout,
  Show,
  TabbedShowLayout,
  TextField,
} from "react-admin"

import {TeamMembersList} from "./MembersList"

export const TeamShow = () => (
  <Show>
    <TabbedShowLayout>
      <TabbedShowLayout.Tab label="summary">
        <TextField
          source="id"
          label="ID"
          aria-readonly={true}
        />
        <TextField source="name" />
        <TextField source="email" />
        <TextField source="description" />
        {/* <TextField source="preferred_name" />
                <TextField source="full_name" />
                <EmailField source="email" />
                <DateField source="date_joined" /> */}
      </TabbedShowLayout.Tab>
      <TabbedShowLayout.Tab label="members">
        <TeamMembersList />
      </TabbedShowLayout.Tab>
    </TabbedShowLayout>
  </Show>
)
