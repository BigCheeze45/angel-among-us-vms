from django.urls import path, include

from rest_framework import routers

from app.views.UserViewSet import UserViewSet
from app.views.SkillCategoryView import SkillCategoryViewSet
from app.views.TeamCategoryViewSet import TeamCategoryViewSet
from app.views.VolunteerSkillView import VolunteerSkillViewSet
from app.views.VolunteerTeamViewSet import VolunteerTeamViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register("volunteers", UserViewSet)
router.register("skills", SkillCategoryViewSet , basename="skills")
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
        # Skills of specific volunteers
        "volunteers/<int:pk>/skills/",
        VolunteerSkillViewSet.as_view({"get": "list"}),
        name="volunteer-skills-list",
    ),
]
