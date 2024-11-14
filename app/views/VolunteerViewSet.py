import uuid
from http import HTTPMethod

import pandas as pd

from rest_framework import viewsets
from django.http import FileResponse
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from rest_framework.exceptions import ValidationError

from app.models.Volunteer import Volunteer
from app.models.VolunteerTeam import VolunteerTeam
from app.serializer.VolunteerSerializer import VolunteerSerializer


class VolunteerFilters(filters.FilterSet):
    class Meta:
        model = Volunteer
        fields = ["active", "job_title", "county"]

    skill = filters.CharFilter(method="filter_by_skill")
    interest = filters.CharFilter(method="filter_by_interest")
    date_joined = filters.DateFromToRangeFilter()
    has_maddie_certification = filters.BooleanFilter(
        field_name="maddie_certifications_received_date", lookup_expr="isnull"
    )
    county_isnull = filters.BooleanFilter(
        field_name="maddie_certifications_received_date", lookup_expr="isnull"
    )

    def filter_by_interest(self, queryset, name, value):
        return self.filter_by_skill(queryset, name, value)

    def filter_by_skill(self, queryset, name, value):
        return (
            queryset.filter(skills__skill__icontains=value, skills__type=name)
            if name in ["skill", "interest"]
            else queryset
        )


class VolunteerViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerSerializer
    filterset_class = VolunteerFilters
    search_fields = [
        "full_name",
        "ishelters_id",
        "preferred_name",
    ]
    export_fields = ["full_name", "email", "job_title", "application_received_date"]

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
        if "application_received_date" in fields:
            df = df.rename(columns={"application_received_date": "last_updated"})
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
        if "application_received_date" in fields:
            df = df.rename(columns={"application_received_date": "last_updated"})
            # Excel does not support datetimes with timezones. Ensure that
            # datetimes are timezone unaware before writing to Excel.
            df["last_updated"] = df["last_updated"].apply(
                lambda dt: pd.to_datetime(dt).date()
            )
        # Once a workbook has been saved it is not possible to write
        # further data without rewriting the whole workbook
        tmp_file = f"/tmp/{str(uuid.uuid4())}.xlsx"
        df.to_excel(tmp_file, index=False, engine="openpyxl")

        return FileResponse(
            open(tmp_file, "rb"),
            as_attachment=True,
            filename=filename,
        )
