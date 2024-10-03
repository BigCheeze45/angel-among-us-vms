from rest_framework import serializers

from app.models.County import County


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = "__all__"

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
