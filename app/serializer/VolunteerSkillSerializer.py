from rest_framework import serializers
from app.models.VolunteerSkill import VolunteerSkill


class VolunteerSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerSkill
        fields = [
            "id",
            "skill",
            "volunteer",
            # "description",
        ]

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
