from django.urls import path, include
from rest_framework import routers
from app.views.VolunteerActivityViewSet import VolunteerActivityViewSet
from app.views.UserViewSet import UserViewSet
from app.views import VolunteerMilestoneViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("volunteer/activity", VolunteerActivityViewSet)
router.register("volunteer/milestones", VolunteerMilestoneViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path("", include(router.urls)),
]
