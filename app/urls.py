from django.urls import path, include

from rest_framework import routers
from app.views.UserViewSet import UserViewSet
from app.views.TeamViewSet import TeamViewSet
from app.views.VolunteerViewSet import VolunteerViewSet
from app.views.TeamCategoryViewSet import TeamCategoryViewSet
from app.views.VolunteerSkillView import VolunteerSkillViewSet
from app.views.SkillCategoryViewSet import SkillCategoryViewSet
from app.views.VolunteerTeamViewSet import VolunteerTeamViewSet
from app.views.VolunteerActivityViewSet import VolunteerActivityViewSet
from app.views.VolunteerMilestoneViewSet import VolunteerMilestoneViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("teams", TeamViewSet)
router.register("volunteers", VolunteerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        # Team of specific volunteers
        "volunteers/<int:pk>/teams/",
        VolunteerTeamViewSet.as_view({"get": "list"}),
        name="volunteer-teams-list",
    ),
    path(
        # Milestones for a specific volunteer
        "volunteers/<int:pk>/milestones/",
        VolunteerMilestoneViewSet.as_view(
            {"get": "list", "post": "create", "patch": "partial_update"}
        ),
        name="volunteer-milestones-list",
    ),
    path(
        # Activities for a specific volunteer
        "volunteers/<int:pk>/activities/",
        VolunteerActivityViewSet.as_view(
            {"get": "list", "post": "create", "patch": "partial_update"}
        ),
        name="volunteer-activities-list",
    ),
    path(
        # Skills of specific volunteers
        "volunteers/<int:pk>/skills/",
        VolunteerSkillViewSet.as_view({"get": "list", "post": "create"}),
        name="volunteer-skills-list",
    ),
    path(
        # endpoint dealing with volunteer skill categories
        "volunteers/skills/categories",
        SkillCategoryViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="skills-categories",
    ),
    path(
        # endpoint dealing with team categories
        "teams/categories",
        TeamCategoryViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="team-categories",
    ),
]
