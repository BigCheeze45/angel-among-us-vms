import uuid
from http import HTTPMethod

from django.http import FileResponse
from django.contrib.auth.models import User

import pandas as pd

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from app.serializer.UserSerializer import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    filterset_fields = [
        "is_staff",
        "is_active",
        "is_superuser",
    ]
    search_fields = [
        "email",
        "username",
        "last_name",
        "first_name",
    ]
    export_fields = ["first_name", "last_name", "email"]

    @action(detail=False, methods=[HTTPMethod.POST, HTTPMethod.GET])
    def export(self, request):
        export_format = request.data.get("format")
        if export_format:
            export_format = export_format.lower()

        if export_format not in ["csv", "excel"]:
            raise ValidationError("Format must be either csv or excel")

        queryset = self.filter_queryset(self.get_queryset())
        ids = request.data.get("ids")
        if ids:
            # user has selected specific IDs to export so only select those
            queryset = queryset.filter(id__in=ids)

        if export_format == "excel":
            return self._create_return_excel(queryset)

        return self._create_return_csv(queryset)

    def get_queryset(self):
        ordering = self.request.query_params.get(
            "ordering", "id"  # default to id is ordering is not specified
        )

        queryset = User.objects.all()

        # apply ordering/sorting
        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset

    def _create_return_csv(
        self, queryset, fields: list[str] = None, filename: str = None
    ):
        if fields is None:
            fields = self.export_fields

        if filename is None:
            filename = "users.csv"

        df = pd.DataFrame(queryset.values(*fields))
        tmp_file = (
            f"/tmp/{str(uuid.uuid4())}.csv"  # write to a temp file with a random name
        )
        df.to_csv(tmp_file, index=False)

        # https://docs.djangoproject.com/en/5.1/ref/request-response/#fileresponse-objects
        return FileResponse(
            open(tmp_file, "rb"),
            as_attachment=True,
            filename=filename,
        )

    def _create_return_excel(
        self, queryset, fields: list[str] = None, filename: str = None
    ):
        if fields is None:
            fields = self.export_fields

        if filename is None:
            filename = "users.xlsx"

        df = pd.DataFrame(queryset.values(*fields))
        # Once a workbook has been saved it is not possible to write
        # further data without rewriting the whole workbook
        tmp_file = f"/tmp/{str(uuid.uuid4())}.xlsx"
        df.to_excel(tmp_file, index=False, engine="openpyxl")

        return FileResponse(
            open(tmp_file, "rb"),
            as_attachment=True,
            filename=filename,
        )
