from rest_framework import serializers

from app.models.Team import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "description", "email", "category"]

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
