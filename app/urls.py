from django.urls import path, include

from rest_framework_nested import routers

from app.views.UserViewSet import UserViewSet
from app.views.TeamViewSet import TeamViewSet
from app.views.VolunteerViewSet import VolunteerViewSet
from app.views.TeamCategoryViewSet import TeamCategoryViewSet
from app.views.VolunteerSkillView import VolunteerSkillViewSet
from app.views.SkillCategoryViewSet import SkillCategoryViewSet
from app.views.VolunteerTeamViewSet import VolunteerTeamViewSet
from app.views.VolunteerActivityViewSet import VolunteerActivityViewSet
from app.views.VolunteerMilestoneViewSet import VolunteerMilestoneViewSet

from app.views.VolunteerPetViewSet import VolunteerPetViewSet
from app.views.VolunteerChildrenViewSet import VolunteerChildrenViewSet

# Create a router and register our top-level viewsets
router = routers.DefaultRouter()
router.register(r"teams", TeamViewSet, basename="Team")
router.register(r"users", UserViewSet, basename="User")
router.register(r"volunteers", VolunteerViewSet, basename="Volunteer")
router.register(r"skills-categories", SkillCategoryViewSet, basename="skillscategories")

# new views routes for children / pet
router.register(r"volunteers-pet", VolunteerPetViewSet, basename="VolunteerPet")
router.register(r"volunteers-childrens", VolunteerChildrenViewSet, basename="VolunteerChildren")

# Create a nested router for team-related views
team_router = routers.NestedSimpleRouter(router, r"teams", lookup="team")
team_router.register(r"members", TeamViewSet, basename="team-members")

# Create a nested router for volunteer-related views
volunteer_router = routers.NestedSimpleRouter(router, r"volunteers", lookup="volunteer")
volunteer_router.register(r"teams", VolunteerTeamViewSet, basename="volunteer-teams")
volunteer_router.register(r"skills", VolunteerSkillViewSet, basename="volunteer-skills")
volunteer_router.register(
    r"milestones", VolunteerMilestoneViewSet, basename="volunteer-milestones"
)
volunteer_router.register(
    r"activities", VolunteerActivityViewSet, basename="volunteer-activities"
)

volunteer_router.register(r"children", VolunteerChildrenViewSet, basename="volunteer-children")
volunteer_router.register(r"pet", VolunteerPetViewSet, basename="volunteer-pet")

# Wire up our API using automatic URL routing
urlpatterns = [
    path("", include(router.urls)),
    path("", include(volunteer_router.urls)),
    path("", include(team_router.urls)),
]
