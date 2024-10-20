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
            "location",
        ]

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
