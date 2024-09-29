from django.urls import path, include
from rest_framework import routers

from app.views.UserViewSet import UserViewSet
from app.views.SkillCategoryView import SkillCategoryViewSet
from .views import VolunteerSkillViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("categories", SkillCategoryViewSet, basename="categories")
router.register("volunteer-skills", VolunteerSkillViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path("", include(router.urls)),
]
