import {PetList} from "./PetList"
import {ShowSummary} from "./ShowSummary"
import {ChildrenList} from "../ChildrenList"
import {VolunteerTeamsList} from "../TeamsList"
import {VolunteerSkillsList} from "../SkillsList"
import {ActivitiesList} from "./VolunteerActivitiesList"
import {Show, TabbedShowLayout, TextField} from "react-admin"

export const VolunteerShow = () => (
  <Show>
    <TabbedShowLayout>
      <TabbedShowLayout.Tab label="summary">
        <ShowSummary />
      </TabbedShowLayout.Tab>
      <TabbedShowLayout.Tab label="teams">
        <VolunteerTeamsList />
      </TabbedShowLayout.Tab>
      <TabbedShowLayout.Tab label="skills/interests">
        <VolunteerSkillsList />
      </TabbedShowLayout.Tab>
      <TabbedShowLayout.Tab label="activities">
        <ActivitiesList />
      </TabbedShowLayout.Tab>
      <TabbedShowLayout.Tab label="Children">
        <ChildrenList />
      </TabbedShowLayout.Tab>
      <TabbedShowLayout.Tab label="Pets">
        <PetList />
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
