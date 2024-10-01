from rest_framework import serializers
from django.contrib.auth.models import User

from app.models.Team import Team
from app.models.Volunteer import Volunteer


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        # include all fields except the following
        exclude = [
            "ishelters_created_dt",
            "application_received_date",
        ]

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
