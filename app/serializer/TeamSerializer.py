from rest_framework import serializers
from app.models.Team import Team


class TeamCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = []
