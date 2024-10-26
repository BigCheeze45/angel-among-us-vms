import uuid
from http import HTTPMethod

from django.http import FileResponse

import pandas as pd

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from app.models.Volunteer import Volunteer
from app.models.VolunteerTeam import VolunteerTeam
from app.serializer.VolunteerSerializer import VolunteerSerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerSerializer
    filterset_fields = [
        "active",
        "ishelters_access_flag",
        "ishelters_category_type",
        "has_maddie_certifications",
        "maddie_certifications_received_date",
    ]
    search_fields = [
        "full_name",
        "preferred_name",
    ]
    export_fields = ["full_name", "email"]

    @action(detail=False, methods=[HTTPMethod.POST, HTTPMethod.GET])
    def export(self, request):
        export_format = request.data.get("format")

        # casefold format for simpler comparison
        if export_format:
            export_format = export_format.lower()

        if export_format not in ["csv", "excel"]:
            raise ValidationError("Format must be either csv or excel")

        # apply URL query param filters (team, county, maddie certs., ect..)
        queryset = self.filter_queryset(self.get_queryset())

        ids = request.data.get("ids")
        if ids:
            # user has selected specific IDs to export so only select those
            queryset = queryset.filter(id__in=ids)

        if export_format == "excel":
            return self._create_return_excel(queryset)

        return self._create_return_csv(queryset)

    def get_queryset(self):
        queryset = Volunteer.objects.all()

        team_id = self.request.query_params.get("team_id")
        if team_id:
            # return only volunteers on this team
            volunteer_ids = VolunteerTeam.objects.filter(team_id=team_id).values_list(
                "volunteer_id", flat=True
            )
            queryset = queryset.filter(id__in=volunteer_ids)

        county = self.request.query_params.get("county")
        if county:
            if county.lower() == "undefined":
                # return volunteers with no address on file
                queryset = Volunteer.objects.filter(
                    county=""
                ) | Volunteer.objects.filter(county__isnull=True)
            else:
                # return volunteers based on their county
                queryset = queryset.filter(county=county)

        # apply ordering, order by ID if not specified
        ordering = self.request.query_params.get("ordering", "id")
        queryset = queryset.order_by(ordering)

        return queryset

    def _create_return_csv(
        self, queryset, fields: list[str] = None, filename: str = None
    ):
        if fields is None:
            fields = self.export_fields

        if filename is None:
            filename = "volunteers.csv"

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
            filename = "volunteers.xlsx"

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
