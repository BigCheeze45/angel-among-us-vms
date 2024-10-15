from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from app.models.Volunteer import Volunteer
from app.models.VolunteerActivity import VolunteerActivity
from app.serializer.VolunteerActivitySerializer import VolunteerActivitySerializer


# ViewSets define the view behavior.
class VolunteerActivityViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerActivitySerializer

    def get_queryset(self):
        queryset = VolunteerActivity.objects.all()

        # Check if we're accessing activities for a specific volunteer
        volunteer_id = self.kwargs.get("volunteer_pk")
        if volunteer_id:
            volunteer = get_object_or_404(Volunteer, id=volunteer_id)
            queryset = queryset.filter(volunteer=volunteer)

        # Apply ordering, order by ID if not specified
        ordering = self.request.query_params.get("ordering", "id")
        queryset = queryset.order_by(ordering)

        return queryset
