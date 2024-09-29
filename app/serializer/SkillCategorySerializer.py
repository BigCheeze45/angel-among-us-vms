from rest_framework import serializers
from app.models.SkillCategory import SkillCategory


class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = ["id", "category", "description"]

    def is_valid(self, *, raise_Exception=True):
        return super().is_valid(raise_exception=raise_Exception)
