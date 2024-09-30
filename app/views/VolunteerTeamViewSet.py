from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from app.models.VolunteerTeam import VolunteerTeam
from app.serializer.VolunteerTeamSerializer import VolunteerTeamSerializer


class VolunteerTeamViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VolunteerTeamSerializer

    def get_queryset(self):
        volunteer_id = self.kwargs.get("pk")
        return VolunteerTeam.objects.filter(volunteer=volunteer_id)

    def retrieve(self, request: Request, pk=None, *args, **kwargs):
        team = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(team)
        return Response(serializer.data)
