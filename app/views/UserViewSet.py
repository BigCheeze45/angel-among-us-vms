from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from django.db.utils import Error as DjangoDBError

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from common.exceptions import ConflictError
from common.utils import django_db_error_parser
from app.serializer.UserSerializer import UserSerializer, UserCreateSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    filterset_fields = [
        "is_staff",
        "is_active",
    ]
    search_fields = [
        "email",
        "username",
        "last_name",
        "first_name",
    ]

    def create(self, request, *args, **kwargs):
        user_create_serializer = UserCreateSerializer(data=request.data)
        # validate the incoming data & abort if it's not valid
        user_create_serializer.is_valid()

        try:
            validated_data = user_create_serializer.data
            # TODO
            # check if this role (group) exists
            # group = get_object_or_404(Group, name__iexact=validated_data["role"])
            # del validated_data["role"]

            user = User.objects.create(
                is_superuser=False,
                **validated_data,
                username=user_create_serializer["email"],
            )
            user.set_unusable_password()
            user.save()

            # TODO
            # assign role to user
            # group.user_set.add(user)

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

    def get_queryset(self):
        ordering = self.request.query_params.get("ordering", "id")

        queryset = User.objects.all()

        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset
