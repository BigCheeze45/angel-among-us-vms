from django.contrib.auth.models import User

from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView as KnoxLogoutView
from knox.views import LogoutAllView as KnoxLogoutAllView

from rest_framework import exceptions
from rest_framework.authentication import BasicAuthentication as DRFBasicAuthentication


class BasicAuthentication(DRFBasicAuthentication):
    """Basic Auth using email (username/userid) only"""

    def authenticate_credentials(self, userid, password=None, request=None):
        try:
            # Lookup users by username (which is their email)
            user = User.objects.get(username=userid)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(("Invalid username/password."))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(("User inactive or deleted."))

        return (user, None)


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]

    def get_post_response_data(self, request, token, instance):
        data = super().get_post_response_data(request, token, instance)

        # load in user roles & permissions
        # so they're returned to the frontend
        data["user"]["permissions"] = request.user.get_all_permissions()
        data["user"]["roles"] = [group.name for group in request.user.groups.all()]
        return data


class LogoutView(KnoxLogoutView):
    pass


class LogoutAllView(KnoxLogoutAllView):
    pass
