import {PetsEdit} from "./PetsEdit"
import {SkillsEdit} from "./SkillsEdit"
import {ChildrenEdit} from "./ChildrenEdit"
import {ActivitiesEdit} from "./ActivitiesEdit"
import {Edit, Toolbar, DateInput, TabbedForm, SaveButton} from "react-admin"

const EditToolbar = () => (
  <Toolbar>
    <SaveButton />
  </Toolbar>
)

export const VolunteerEdit = () => {
  return (
    <Edit>
      <TabbedForm toolbar={<EditToolbar />}>
        <TabbedForm.Tab label="summary">
          <DateInput
            label="Maddie certification date"
            source="maddie_certifications_received_date"
          />
        </TabbedForm.Tab>
        <TabbedForm.Tab label="skills/interests">
          <SkillsEdit />
        </TabbedForm.Tab>
        <TabbedForm.Tab label="activities">
          <ActivitiesEdit />
        </TabbedForm.Tab>
        <TabbedForm.Tab label="Children">
          <ChildrenEdit />
        </TabbedForm.Tab>
        <TabbedForm.Tab label="Pets">
          <PetsEdit />
        </TabbedForm.Tab>
      </TabbedForm>
    </Edit>
  )
}
