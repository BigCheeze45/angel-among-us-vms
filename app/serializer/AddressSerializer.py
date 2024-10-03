from rest_framework import serializers

from app.models.Address import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
