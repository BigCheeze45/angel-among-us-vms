from rest_framework import serializers

from app.models.VolunteerTeam import VolunteerTeam


# Serializers define the API representation.
class VolunteerTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerTeam
        fields = ["id", "team"]

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
