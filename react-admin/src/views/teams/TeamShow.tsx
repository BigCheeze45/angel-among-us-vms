import {TeamMembersList} from "./MembersList"
import {Show, TextField, TabbedShowLayout} from "react-admin"

export const TeamShow = () => (
  <Show>
    <TabbedShowLayout>
      <TabbedShowLayout.Tab label="summary">
        <TextField source="name" />
        <TextField source="email" />
        <TextField source="description" />
      </TabbedShowLayout.Tab>
      <TabbedShowLayout.Tab label="members">
        <TeamMembersList />
      </TabbedShowLayout.Tab>
    </TabbedShowLayout>
  </Show>
)
