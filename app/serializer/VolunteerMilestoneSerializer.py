from rest_framework import serializers
from app.models.VolunteerMilestone import VolunteerMilestone


class VolunteerMilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerMilestone
        fields = [
            "id",
            "volunteer",
            "years_of_service",
            "milestone_date",
            "award_title",
            "award_description",
            "achievement_level",
            "is_active",
        ]

        def is_valid(self, *, raise_Exception=True):
            return super().is_valid(raise_exception=raise_Exception)
