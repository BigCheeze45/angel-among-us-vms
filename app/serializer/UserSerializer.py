from django.contrib.auth.models import User

from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ["password", "username", "is_superuser"]

    def get_role(self, user):
        return [g.name.lower() for g in user.groups.all()]


class UserCreateSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, max_length=155)
    last_name = serializers.CharField(required=True, max_length=155)
    # TODO - use email validator to restrict acceptable domains
    # e.g only @angelresuce.org emails are
    email = serializers.EmailField(required=True)
    is_staff = serializers.BooleanField(required=True)
    is_active = serializers.BooleanField(default=True)
    role = serializers.ChoiceField(
        required=True, choices=["administrator", "viewer", "editor"]
    )

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
