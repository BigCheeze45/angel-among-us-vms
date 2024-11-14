"""
URL configuration for vms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path


from app.views.AuthView import (
    LoginView,
    LogoutView,
    health_check,
    refresh_token,
    LogoutAllView,
)

urlpatterns = [
    path("", include("app.urls")),
    path("admin/", admin.site.urls),
    path(r"status/", health_check, name="health_check"),
    path(r"api/auth/refresh/", refresh_token, name="knox_refresh"),
    path(r"api/auth/login/", LoginView.as_view(), name="knox_login"),
    path(r"api/auth/logout/", LogoutView.as_view(), name="knox_logout"),
    path(r"api/auth/logoutall/", LogoutAllView.as_view(), name="knox_logoutall"),
]

if settings.DEBUG:
    # expose browseable API if in dev/debug mode
    # or any other URLs that should be accessible only during dev
    urlpatterns.append(
        path("api-auth/", include("rest_framework.urls")),
    )
