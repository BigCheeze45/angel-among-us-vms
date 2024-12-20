from http import HTTPMethod

from django.conf import settings
from django.contrib.auth.models import User

from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView as KnoxLogoutView
from knox.views import LogoutAllView as KnoxLogoutAllView

from google.oauth2 import id_token
from google.auth.transport import requests

from rest_framework.response import Response
from rest_framework import exceptions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    BasicAuthentication as DRFBasicAuthentication,
)
import os
import pprint
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)


class BasicAuthentication(DRFBasicAuthentication):
    """Basic Auth using email (username/userid) only"""

    def authenticate_credentials(self, userid, password=None, request=None):
        try:
            idinfo = id_token.verify_oauth2_token(
                userid, requests.Request(), settings.GOOGLE_CLIENT_ID
            )

            if idinfo["aud"] != settings.GOOGLE_CLIENT_ID:
                raise exceptions.AuthenticationFailed(("Invalid token"))

            # If the request specified a Google Workspace domain
            if "hd" in idinfo:
                if idinfo["hd"] != settings.GOOGLE_WORKSPACE_DOMAIN:
                    raise exceptions.AuthenticationFailed(
                        ("Please login with an AAU Google Workspace account")
                    )
            # G token is valid
            username = idinfo["email"]
        except ValueError:
            raise exceptions.AuthenticationFailed(("Invalid token"))

        try:
            # Lookup users by username (which is their email)
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(("Invalid username/password"))

        if not user.is_staff or not user.is_active:
            # Only when both is_staff AND is_active are True does the authentication pass
            raise exceptions.AuthenticationFailed(("User inactive or deleted"))

        return (user, None)


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
    DJANGO_RA_ACTION_MAPPING = {
        "view": ["list", "show"],
        "change": ["edit"],
        "add": ["create"],
        "delete": ["delete"],
    }

    def get_post_response_data(self, request, token, instance):
        print(dir(request))
        print(request.data)
        print(request.auth)
        data = super().get_post_response_data(request, token, instance)

        # build permissions into a format react-admin understands
        # https://marmelab.com/react-admin/AuthRBAC.html
        user_perms = request.user.get_all_permissions()
        # user_perms = [
        #     "auth.change_permission",
        #     "contenttypes.change_contenttype",
        #     "auth.add_user",
        #     "app.delete_volunteerteam",
        #     "app.add_team",
        #     "app.view_volunteeractivity",
        # ]
        ra_perms_dict = []
        for item in user_perms:
            app, perm = item.split(".")
            # FIXME - is there way to get current app label instead of hardcoding
            # in case the name/label changes
            if app in ("app", "auth"):
                action, resource = perm.split("_")
                if resource in ("volunteer", "team", "user"):
                    ra_perms_dict.append(
                        {
                            "action": self.DJANGO_RA_ACTION_MAPPING.get(action, []),
                            "resource": f"{resource}s",
                        }
                    )
        data["user"]["permissions"] = ra_perms_dict
        data["expiry"] = instance.expiry
        # data["user"]["roles"] = [group.name for group in request.user.groups.all()]
        return data


@api_view([HTTPMethod.POST])
def refresh_token(request):
    """Refresh token"""
    return Response(None, status=status.HTTP_200_OK)


@api_view([HTTPMethod.GET])
@authentication_classes([])
@permission_classes([])
def health_check(request):
    """Endpoint to check whether the app is up & running"""
    return Response(None, status=status.HTTP_200_OK)


class LogoutView(KnoxLogoutView):
    pass


class LogoutAllView(KnoxLogoutAllView):
    pass
