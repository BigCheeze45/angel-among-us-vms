from rest_framework import serializers
from app.models.VolunteerChildren import VolunteerChildren


class VolunteerChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerChildren
        fields = [
            "id",
            "volunteer",
            "description",
            "created_at",
            "updated_at",
        ]

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
