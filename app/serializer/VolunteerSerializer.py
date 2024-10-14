from rest_framework import serializers

from app.models.Volunteer import Volunteer
from app.models.VolunteerTeam import VolunteerTeam


class TeamWithStartDateSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="team.id")
    name = serializers.CharField(source="team.name")
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()


class VolunteerSerializer(serializers.ModelSerializer):
    teams = serializers.SerializerMethodField()

    class Meta:
        model = Volunteer
        # include all fields except the following
        exclude = [
            "ishelters_created_dt",
            "application_received_date",
        ]

    def get_teams(self, obj):
        volunteer_teams = VolunteerTeam.objects.filter(volunteer=obj).select_related(
            "team"
        )
        return TeamWithStartDateSerializer(volunteer_teams, many=True).data

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
