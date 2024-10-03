from django.test import TestCase
from django.contrib.auth.models import User

from app.models import VolunteerSkill, SkillCategory


class VolunteerSkillTestCases(TestCase):
    def setUp(self):
        self.volunteer = User.objects.create(
            username="JohnDoe", email="john@example.com"
        )
        self.category = SkillCategory.objects.create(
            category="Communication", description="Communication skills"
        )
        self.test_instance = VolunteerSkill.objects.create(
            volunteer=self.volunteer,
            category=self.category,
            proficiency_level=8,
            years_of_experience=5.0,
            description="Excellent communication skills in various contexts",
        )

    def test_model_creation(self):
        self.assertEqual(VolunteerSkill.objects.count(), 1)
        self.assertEqual(self.test_instance.proficiency_level, 8)
        self.assertEqual(self.test_instance.years_of_experience, 5.0)

    def test_model_update(self):
        self.test_instance.years_of_experience = 10
        self.test_instance.proficiency_level = 4
        self.test_instance.category = SkillCategory.objects.create(category="IT")
        self.test_instance.save()

        instance = VolunteerSkill.objects.get(id=self.test_instance.id)
        self.assertEqual(instance.years_of_experience, 10.0)
        self.assertEqual(instance.proficiency_level, 4)
        self.assertEqual(instance.category.category, "IT")
    

    # def test_volunteer_skill_api(self):
    #     url = reverse(
    #         "volunteer-skill-list"
    #     )  # Assuming the viewset has a basename `volunteer-skill`
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)

    # def test_create_volunteer_skill_via_api(self):
    #     url = reverse("volunteer-skill-list")
    #     data = {
    #         "volunteer": self.volunteer.id,
    #         "category": self.category.id,
    #         "proficiency_level": 9,
    #         "years_of_experience": 7.5,
    #         "verified": False,
    #         "date_acquired": "2018-03-01",
    #         "description": "Strong leadership and communication",
    #         "certificate_url": "http://example.com/certificate2.jpg",
    #     }
    #     response = self.client.post(url, data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(VolunteerSkill.objects.count(), 2)
