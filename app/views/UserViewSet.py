from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from app.serializer.UserSerializer import UserSerializer


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

    def create(self, request, *args, **kwargs):
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        if not email:
            raise ValidationError({"email": "This field is required."})

        user = User(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_superuser=False,
        )

        try:
            user.save()
            user.set_unusable_password()
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        ordering = self.request.query_params.get("ordering", "id")

        queryset = User.objects.all()

        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset
