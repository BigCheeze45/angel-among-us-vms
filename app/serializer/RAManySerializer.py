from rest_framework import serializers


class PaginationField(serializers.DictField):
    def to_internal_value(self, data):
        # First, validate as a dict
        dict_value = super().to_internal_value(data)

        # Now, validate page and per_page
        page = dict_value.get("page", 1)
        per_page = dict_value.get("per_page", 25)

        # Ensure page and per_page are integers
        try:
            page = int(page)
            per_page = int(per_page)
        except ValueError:
            raise serializers.ValidationError("'page' and 'per_page' must be integers.")

        # Ensure positive values
        if page < 1 or per_page < 1:
            raise serializers.ValidationError(
                "'page' and 'per_page' must be positive integers."
            )

        # Update the dict with validated and defaulted values
        dict_value["page"] = page
        dict_value["per_page"] = per_page

        return dict_value


class RAManySerializer(serializers.Serializer):
    """
    A serializer for react-admin data provider getMany request, which provides a
    list of IDs to operate on.
    """

    data = serializers.DictField(required=False, allow_empty=True)
    pagination = PaginationField(required=False, allow_empty=True)
    ids = serializers.ListField(child=serializers.IntegerField(), allow_empty=False)

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
