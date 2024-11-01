from django.urls import path, include

from rest_framework_nested import routers

from app.views.UserViewSet import UserViewSet
from app.views.TeamViewSet import TeamViewSet
from app.views.VolunteerViewSet import VolunteerViewSet
from app.views.VolunteerSkillView import VolunteerSkillViewSet
from app.views.VolunteerTeamViewSet import VolunteerTeamViewSet
from app.views.VolunteerActivityViewSet import VolunteerActivityViewSet

# Create a router and register our top-level viewsets
router = routers.DefaultRouter()
router.register(r"teams", TeamViewSet, basename="Team")
router.register(r"users", UserViewSet, basename="User")
router.register(r"volunteers", VolunteerViewSet, basename="Volunteer")

# Create a nested router for team-related views
team_router = routers.NestedSimpleRouter(router, r"teams", lookup="team")
team_router.register(r"members", TeamViewSet, basename="team-members")

# Create a nested router for volunteer-related views
volunteer_router = routers.NestedSimpleRouter(router, r"volunteers", lookup="volunteer")
volunteer_router.register(r"teams", VolunteerTeamViewSet, basename="volunteer-teams")
volunteer_router.register(r"skills", VolunteerSkillViewSet, basename="volunteer-skills")
volunteer_router.register(
    r"activities", VolunteerActivityViewSet, basename="volunteer-activities"
)

# Wire up our API using automatic URL routing
urlpatterns = [
    path("", include(router.urls)),
    path("", include(volunteer_router.urls)),
    path("", include(team_router.urls)),
]
