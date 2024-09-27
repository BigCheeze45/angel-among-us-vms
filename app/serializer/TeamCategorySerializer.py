from rest_framework import serializers

from app.models.TeamCategory import TeamCategory


# Serializers define the API representation.
class TeamCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCategory
        fields = ["id", "name"]

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
