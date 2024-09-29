from django.test import TestCase
from app.models import Volunteer, VolunteerMilestone
import uuid
from django.utils import timezone


class VolunteerMilestoneModelTest(TestCase):

    def setUp(self):
        # Create a volunteer instance
        self.volunteer = Volunteer.objects.create(id=uuid.uuid4(), name="Jane Doe")

        # Create a volunteer milestone instance
        self.milestone = VolunteerMilestone.objects.create(
            volunteer=self.volunteer,
            years_of_service=5,
            milestone_date=timezone.now(),
            award_title="Outstanding Volunteer",
            award_description="Awarded for five years of outstanding service",
            achievement_level="gold",
            is_active=True,
        )

    def test_volunteer_milestone_creation(self):
        self.assertEqual(self.milestone.years_of_service, 5)
        self.assertEqual(self.milestone.volunteer.name, "Jane Doe")
        self.assertEqual(self.milestone.award_title, "Outstanding Volunteer")
        self.assertEqual(self.milestone.achievement_level, "gold")
        self.assertTrue(self.milestone.is_active)

    def test_volunteer_milestone_str_method(self):
        self.assertEqual(str(self.milestone), "Milestone for Jane Doe: 5 years")
