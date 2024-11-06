from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from app.models.Volunteer import Volunteer
from app.models.VolunteerChildren import VolunteerChildren
from app.serializer.VolunteerChildrenSerializer import VolunteerChildrenSerializer


class VolunteerChildrenViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerChildrenSerializer

    def get_queryset(self):
        queryset = VolunteerChildren.objects.all()

        volunteer_id = self.kwargs.get("volunteer_pk")
        if volunteer_id:
            volunteer = get_object_or_404(Volunteer, id=volunteer_id)
            queryset = queryset.filter(volunteer=volunteer)

        # Apply ordering, order by ID if not specified
        ordering = self.request.query_params.get("ordering", "id")
        queryset = queryset.order_by(ordering)

        return queryset

    def retrieve(self, request: Request, pk=None, *args, **kwargs):
        team = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(team)
        return Response(serializer.data)
