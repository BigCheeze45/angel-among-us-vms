from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from django.core.exceptions import ObjectDoesNotExist

from app.models.Team import Team
from app.models.TeamCategory import TeamCategory
from app.serializer.TeamCategorySerializer import TeamCategorySerializer


class TeamCategoryTestCases(APITestCase):
    """
    Test TeamCategory View set (API)
    """

    def setUp(self):
        # Create a new TeamCategory to start the test
        self.test_instance = TeamCategory.objects.create(name="Admin")

    def test_api_list(self):
        url = reverse("categories-list")
        response = self.client.get(url)
        expected = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [{"id": self.test_instance.id, "name": "Admin"}],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data, expected)

    def test_api_create(self):
        payload = {"name": "API Category"}
        url = reverse("categories-list")
        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        api_instance = TeamCategory.objects.get(name="API Category")
        payload["id"] = api_instance.id
        self.assertEqual(response.data, payload)

    def test_api_create_invalid(self):
        payload = {"Not_Name": "API Category"}
        url = reverse("categories-list")
        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_update(self):
        payload = TeamCategorySerializer(self.test_instance).data
        payload["name"] = "New Category Name"
        url = reverse(f"categories-detail", kwargs={"pk": payload["id"]})

        response = self.client.patch(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, payload)

    def test_api_delete_when_in_use(self):
        """Test deleting a category when it is assigned to a team (should not be possible)"""
        _ = Team.objects.create(
            name="Team Name",
            email="team_email@example.org",
            category=self.test_instance,
            description="A very nice long description",
        )

        instance_id = self.test_instance.id
        url = reverse(f"categories-detail", kwargs={"pk": instance_id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_api_delete(self):
        instance_id = self.test_instance.id
        url = reverse(f"categories-detail", kwargs={"pk": instance_id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Try getting the deleted model by ID
        with self.assertRaises(ObjectDoesNotExist):
            TeamCategory.objects.get(id=instance_id)
