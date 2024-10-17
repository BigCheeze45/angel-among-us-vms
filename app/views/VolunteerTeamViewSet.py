from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from app.models.Volunteer import Volunteer
from app.models.VolunteerTeam import VolunteerTeam
from app.serializer.VolunteerTeamSerializer import VolunteerTeamSerializer


class VolunteerTeamViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerTeamSerializer

    def get_queryset(self):
        queryset = VolunteerTeam.objects.all()

        volunteer_id = self.kwargs.get("volunteer_pk")
        if volunteer_id:
            volunteer = get_object_or_404(Volunteer, id=volunteer_id)
            queryset = queryset.filter(volunteer=volunteer)

        # Apply ordering, order by ID if not specified
        ordering = self.request.query_params.get("ordering", "id")
        queryset = queryset.order_by(ordering)

        return queryset

    def perform_create(self, serializer):
        volunteer_pk = self.kwargs.get("volunteer_pk")
        volunteer = get_object_or_404(Volunteer, pk=volunteer_pk)
        serializer.save(volunteer=volunteer)

    def retrieve(self, request: Request, pk=None, *args, **kwargs):
        team = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(team)
        return Response(serializer.data)
