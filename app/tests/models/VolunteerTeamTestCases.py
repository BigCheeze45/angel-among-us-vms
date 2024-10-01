from django.test import TestCase
from django.utils.timezone import localtime
from django.core.exceptions import ObjectDoesNotExist

from app.models.Team import Team
from app.models.Volunteer import Volunteer
from app.models.TeamCategory import TeamCategory
from app.models.VolunteerTeam import VolunteerTeam


class VolunteerTeamTestCases(TestCase):
    """
    Test VolunteerTeam model
    """

    def setUp(self):
        # Create a new VolunteerTeam to start the test
        # This includes a Volunteer and Team they're a part of
        # Using User for now until Volunteer model is complete
        self.category = TeamCategory.objects.create(name="Administration")

        self.volunteer = Volunteer.objects.create(
            first_name="John", last_name="Doe", cell_phone="999-999-999"
        )

        self.team = Team.objects.create(
            name="Team Name",
            category=self.category,
            email="team_email@example.org",
            description="A very nice long description",
        )

        # VolunteerTeam
        self.test_instance = VolunteerTeam.objects.create(
            team=self.team, volunteer=self.volunteer
        )

    def test_model_creation(self):
        # Get the created instance from the database
        instance = VolunteerTeam.objects.get(id=self.test_instance.id)

        # test the user (volunteer) & team are correct
        self.assertEqual(instance.team.name, "Team Name")
        self.assertEqual(instance.volunteer.full_name, "John Doe")

    def test_model_str(self):
        self.assertEqual(str(self.test_instance), "John Doe => Team Name")

    def test_model_update_end_date(self):
        # user = User.objects.create(username="NewVolunteer")
        now = localtime()
        self.test_instance.end_date = now
        self.test_instance.save()

        updated_instance = VolunteerTeam.objects.get(id=self.test_instance.id)
        self.assertEqual(updated_instance.end_date, now)

    def test_model_deletion(self):
        instance_id = self.test_instance.id

        # Delete the model
        self.test_instance.delete()

        # Try getting the deleted model by ID
        with self.assertRaises(ObjectDoesNotExist):
            VolunteerTeam.objects.get(id=instance_id)
