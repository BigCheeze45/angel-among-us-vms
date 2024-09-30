from rest_framework import serializers
from app.models.VolunteerActivity import VolunteerActivity


class VolunteerActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerActivity
        fields = [
            "id",
            "volunteer",
            "activity_name",
            "description",
            "start_date",
            "end_date",
            "location",
            "hours_spent",
            "status",
        ]

    def is_valid(self, *, raise_Exception=True):
        return super().is_valid(raise_exception=raise_Exception)
