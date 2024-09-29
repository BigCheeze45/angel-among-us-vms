from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from app.models.Team import Team
from app.models.TeamCategory import TeamCategory
from app.models.VolunteerTeam import VolunteerTeam


class VolunteerTeamTestCases(APITestCase):
    """
    Test TeamCategory View set (API)
    """

    def setUp(self):
        # Create a new VolunteerTeam to start the test
        # This includes a Volunteer and Team they're a part of
        # Using User for now until Volunteer model is complete
        self.category = TeamCategory.objects.create(name="Administration")

        self.user = User.objects.create(username="username")

        self.team = Team.objects.create(
            name="Team Name",
            category=self.category,
            email="team_email@example.org",
            description="A very nice long description",
        )

        # VolunteerTeam
        self.test_instance = VolunteerTeam.objects.create(
            team=self.team, volunteer=self.user
        )

    def test_api_list(self):
        url = reverse("volunteer-teams-list", kwargs={"pk": self.user.id})
        response = self.client.get(url)
        expected = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [{"team": self.team.id, "id": self.test_instance.id}],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data, expected)

    def test_api_create(self):
        url = reverse("volunteer-teams-list", kwargs={"pk": self.user.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_api_update(self):
        url = reverse("volunteer-teams-list", kwargs={"pk": self.user.id})
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_api_delete(self):
        """Test deleting a category when it is assigned to a team (should not be possible)"""
        url = reverse("volunteer-teams-list", kwargs={"pk": self.user.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
