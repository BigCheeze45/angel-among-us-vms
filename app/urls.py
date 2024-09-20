from django.urls import path, include
from rest_framework import routers

from app.views.UserViewSet import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register("users", UserViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path("", include(router.urls)),
]
