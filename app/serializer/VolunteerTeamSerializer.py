from rest_framework import serializers

from app.models.VolunteerTeam import VolunteerTeam


# Serializers define the API representation.
class VolunteerTeamSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name')
    team_id = serializers.IntegerField(source='team.id')

    class Meta:
        model = VolunteerTeam
        fields = ["id", "team_id", "team_name"]

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
