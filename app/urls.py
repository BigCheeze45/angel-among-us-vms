from django.urls import path, include

from rest_framework import routers
from app.views.UserViewSet import UserViewSet
from app.views.SkillCategoryView import SkillCategoryViewSet
from app.views.TeamCategoryViewSet import TeamCategoryViewSet
from app.views.VolunteerSkillView import VolunteerSkillViewSet
from app.views.VolunteerTeamViewSet import VolunteerTeamViewSet
from app.views.VolunteerActivityViewSet import VolunteerActivityViewSet
from app.views.VolunteerMilestoneViewSet import VolunteerMilestoneViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register("users", UserViewSet)
router.register("volunteers", UserViewSet)
router.register("skills", SkillCategoryViewSet, basename="skills")
router.register("categories", TeamCategoryViewSet, basename="categories")

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
]
