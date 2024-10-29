from rest_framework import serializers

from app.models.Team import Team
from app.models.VolunteerTeam import VolunteerTeam


class VolunteerWithStartDateSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="volunteer.id")
    email = serializers.CharField(source="volunteer.email")
    full_name = serializers.CharField(source="volunteer.full_name")
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()


class TeamSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ["id", "name", "description", "email", "members"]

    def get_members(self, obj):
        volunteer_teams = VolunteerTeam.objects.filter(team=obj).select_related(
            "volunteer"
        )
        return VolunteerWithStartDateSerializer(volunteer_teams, many=True).data

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
