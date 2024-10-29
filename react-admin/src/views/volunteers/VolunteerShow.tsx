import {Show, TabbedShowLayout, TextField} from "react-admin"
import {VolunteerTeamsList} from "./TeamsList"
import {VolunteerSkillsList} from "./SkillsList"
import {VolunteerShowSummary} from "./VolunteerShowSummary"
import {VolunteerActivitiesList} from "./VolunteerActivitiesList"

export const VolunteerShow = () => (
  <Show>
    <TabbedShowLayout>
      <TabbedShowLayout.Tab label="summary">
        <VolunteerShowSummary />
      </TabbedShowLayout.Tab>
      <TabbedShowLayout.Tab label="teams">
        <VolunteerTeamsList />
      </TabbedShowLayout.Tab>
      <TabbedShowLayout.Tab label="skills/interests">
        <VolunteerSkillsList />
      </TabbedShowLayout.Tab>
      <TabbedShowLayout.Tab label="activities">
        <VolunteerActivitiesList />
      </TabbedShowLayout.Tab>
      <TabbedShowLayout.Tab label="address">
        <TextField source="address_line_1" />
        <TextField source="address_line_2" />
        <TextField source="city" />
        <TextField source="state" />
        <TextField source="county" />
        <TextField source="zipcode" />
      </TabbedShowLayout.Tab>
    </TabbedShowLayout>
  </Show>
)
