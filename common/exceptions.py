from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException


class ConflictError(APIException):
    default_code = "conflict"
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Request conflicts with the current state of the target resource"
