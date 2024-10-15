import { Show, TabbedShowLayout, RichTextField } from 'react-admin'
import { VolunteerTeamsList } from "./TeamsList"
import { VolunteerMilestonesList } from "./MilestonesList"
import { VolunteerShowSummary } from './VolunteerShowSummary'
import { VolunteerActivitiesList } from "./VolunteerActivitiesList"

export const VolunteerShow = () => (
    <Show>
        <TabbedShowLayout>
            <TabbedShowLayout.Tab label="summary">
                <VolunteerShowSummary />
            </TabbedShowLayout.Tab>
            <TabbedShowLayout.Tab label="activities">
                <VolunteerActivitiesList />
            </TabbedShowLayout.Tab>
            <TabbedShowLayout.Tab label="teams">
                <VolunteerTeamsList />
            </TabbedShowLayout.Tab>
            <TabbedShowLayout.Tab label="milestones">
                <VolunteerMilestonesList />
            </TabbedShowLayout.Tab>
            <TabbedShowLayout.Tab label="address">
                <RichTextField source="body" label={false} />
            </TabbedShowLayout.Tab>
        </TabbedShowLayout>
    </Show>
)
