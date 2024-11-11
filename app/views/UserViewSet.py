import uuid
from http import HTTPMethod

from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from django.db.utils import Error as DjangoDBError
import pandas as pd

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.exceptions import APIException, ValidationError, PermissionDenied

from common.exceptions import ConflictError
from common.utils import django_db_error_parser
from app.serializer.UserSerializer import UserSerializer, UserCreateSerializer


class UserFilters(filters.FilterSet):
    # role = filters.BooleanFilter(name="date_published", method="filter_is_published")

    class Meta:
        model = User
        fields = ["is_staff", "is_active"]


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    filterset_class = UserFilters

    search_fields = [
        "email",
        "username",
        "last_name",
        "first_name",
    ]
    export_fields = ["first_name", "last_name", "email", "is_staff", "is_active"]

    def destroy(self, request, *args, **kwargs):
        if not request.user.has_perm("auth.delete_user"):
            raise PermissionDenied("You do not have permission to delete this user.")
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.has_perm("auth.change_user"):
            raise PermissionDenied("You do not have permission to update this user.")
        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # Returns True if the user has the specified permission, where perm is in the format "<app label>.<permission codename>".
        if not request.user.has_perm("auth.add_user"):
            raise PermissionDenied("You do not have permission to create a user.")

        user_create_serializer = UserCreateSerializer(data=request.data)
        # validate the incoming data & abort if it's not valid
        user_create_serializer.is_valid()

        try:
            validated_data = user_create_serializer.data

            # check if this role (group) exists
            group = get_object_or_404(Group, name__iexact=validated_data["role"])
            del validated_data["role"]

            user = User.objects.create(
                is_superuser=False,
                **validated_data,
                username=user_create_serializer["email"],
            )
            user.set_unusable_password()
            user.save()

            # assign role to user
            group.user_set.add(user)

            # return everything
            serializer = self.serializer_class(user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except DjangoDBError as e:
            parsed_e = django_db_error_parser(e)
            if (
                parsed_e
                and "duplicate key value violates unique constraint" in parsed_e.slug
            ):
                raise ConflictError(
                    detail=f"User with {'email' if parsed_e.field == 'username' else parsed_e.field} already exist"
                )

            # return a general API error
            raise APIException()

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
        ordering = self.request.query_params.get("ordering", "id")

        queryset = User.objects.all()

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
