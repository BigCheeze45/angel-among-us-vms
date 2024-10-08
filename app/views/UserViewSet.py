from django.contrib.auth.models import User

from rest_framework import viewsets

from app.serializer.UserSerializer import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        ordering = self.request.query_params.get(
            "ordering", "id"  # default to id is ordering is not specified
        )

        queryset = User.objects.all()

        # apply ordering/sorting
        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset
