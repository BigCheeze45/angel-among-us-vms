from django.urls import path, include
from rest_framework import routers

from app.views.UserViewSet import UserViewSet
from app.views.TeamViewSet import TeamViewSet
from app.views.VolunteerViewSet import VolunteerViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register("teams", TeamViewSet)
router.register("users", UserViewSet)
router.register("volunteers", VolunteerViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path("", include(router.urls)),
]
