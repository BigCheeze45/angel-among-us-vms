from rest_framework import viewsets

from app.models.Volunteer import Volunteer
from app.serializer.VolunteerSerializer import VolunteerSerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerSerializer
    filterset_fields = [
        "active",
        "has_maddie_certifications",
        "maddie_certifications_received_date",
    ]
    search_fields = [
        "full_name",
        "preferred_name",
    ]

    def get_queryset(self):
        queryset = Volunteer.objects.all()

        # apply ordering, order by ID if not specified
        ordering = self.request.query_params.get("ordering", "id")
        queryset = queryset.order_by(ordering)

        return queryset
