from django.contrib.auth.models import User
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ["id", "url", "username", "email", "is_staff"]
        fields = "__all__"
