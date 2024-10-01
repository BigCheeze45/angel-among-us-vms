from django.test import TestCase
from app.models import Volunteer, VolunteerActivity
import uuid
from django.utils import timezone


class VolunteerActivityModelTest(TestCase):

    def setUp(self):
        # Create a volunteer instance
        self.volunteer = Volunteer.objects.create(id=uuid.uuid4(), name="John Doe")

        # Create a volunteer activity instance
        self.activity = VolunteerActivity.objects.create(
            volunteer=self.volunteer,
            activity_name="Community Cleanup",
            description="Cleaning the local park",
            start_date=timezone.now(),
            end_date=timezone.now(),
            location="Central Park",
            hours_spent=5.0,
            status="completed",
        )

    def test_volunteer_activity_creation(self):
        self.assertEqual(self.activity.activity_name, "Community Cleanup")
        self.assertEqual(self.activity.volunteer.name, "John Doe")
        self.assertEqual(self.activity.location, "Central Park")
        self.assertEqual(self.activity.hours_spent, 5.0)
        self.assertEqual(self.activity.status, "completed")

    def test_volunteer_str_method(self):
        self.assertEqual(str(self.activity), "Community Cleanup by John Doe")
