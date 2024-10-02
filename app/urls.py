from django.urls import path, include
from rest_framework_nested import routers
from app.views.UserViewSet import UserViewSet
from app.views.TeamViewSet import TeamViewSet
from app.views.AddressViewSet import AddressViewSet
from app.views.VolunteerViewSet import VolunteerViewSet
from app.views.VolunteerSkillView import VolunteerSkillViewSet
from app.views.VolunteerTeamViewSet import VolunteerTeamViewSet
from app.views.VolunteerActivityViewSet import VolunteerActivityViewSet

# Create a router and register our top-level viewsets
router = routers.DefaultRouter()
router.register(r"teams", TeamViewSet)
router.register(r"users", UserViewSet)
router.register(r"volunteers", VolunteerViewSet)

# Create a nested router for volunteer-related views
volunteer_router = routers.NestedSimpleRouter(router, r"volunteers", lookup="volunteer")
volunteer_router.register(r"address", AddressViewSet, basename="volunteer-address")
volunteer_router.register(r"teams", VolunteerTeamViewSet, basename="volunteer-teams")
volunteer_router.register(r"skills", VolunteerSkillViewSet, basename="volunteer-skills")
volunteer_router.register(
    r"activities", VolunteerActivityViewSet, basename="volunteer-activities"
)

# Wire up our API using automatic URL routing
urlpatterns = [
    path("", include(router.urls)),
    path("", include(volunteer_router.urls)),
]
