from rest_framework import serializers
from app.models.VolunteerSkill import VolunteerSkill


class VolunteerSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerSkill
        fields = [
            "id",
            "volunteer",
            "category",
            "proficiency_level",
            "years_of_experience",
            "verified",
            "date_acquired",
            "description",
            "certificate_url",
            "created_at",
            "updated_at",
        ]

    def is_valid(self, *, raise_Exception=True):
        return super().is_valid(raise_exception=raise_Exception)
