from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from app.models import VolunteerSkill, Volunteer, SkillCategory
from datetime import date


class VolunteerSkillTestCase(TestCase):
    def setUp(self):
        self.volunteer = Volunteer.objects.create(
            name="John Doe", email="john@example.com"
        )
        self.category = SkillCategory.objects.create(
            category="Communication", description="Communication skills"
        )
        self.volunteer_skill = VolunteerSkill.objects.create(
            volunteer=self.volunteer,
            category=self.category,
            proficiency_level=8,
            years_of_experience=5.0,
            verified=True,
            date_acquired=date(2015, 6, 15),
            description="Excellent communication skills in various contexts",
            certificate_url="http://example.com/certificate.jpg",
        )
        self.client = APIClient()

    def test_volunteer_skill_creation(self):
        self.assertEqual(VolunteerSkill.objects.count(), 1)
        self.assertEqual(self.volunteer_skill.proficiency_level, 8)
        self.assertEqual(self.volunteer_skill.years_of_experience, 5.0)
        self.assertTrue(self.volunteer_skill.verified)

    def test_volunteer_skill_api(self):
        url = reverse(
            "volunteer-skill-list"
        )  # Assuming the viewset has a basename `volunteer-skill`
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_volunteer_skill_via_api(self):
        url = reverse("volunteer-skill-list")
        data = {
            "volunteer": self.volunteer.id,
            "category": self.category.id,
            "proficiency_level": 9,
            "years_of_experience": 7.5,
            "verified": False,
            "date_acquired": "2018-03-01",
            "description": "Strong leadership and communication",
            "certificate_url": "http://example.com/certificate2.jpg",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VolunteerSkill.objects.count(), 2)
