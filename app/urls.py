from django.urls import path, include

from rest_framework import routers

from app.views.UserViewSet import UserViewSet
from app.views.TeamCategoryViewSet import TeamCategoryViewSet
from app.views.VolunteerTeamViewSet import VolunteerTeamViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register("volunteers", UserViewSet)
router.register("categories", TeamCategoryViewSet, basename="categories")

urlpatterns = [
    path("", include(router.urls)),
    path(
        # Team of specific volunteers
        "volunteers/<int:pk>/teams/",
        VolunteerTeamViewSet.as_view({"get": "list"}),
        name="volunteer-teams-list",
    ),
]
