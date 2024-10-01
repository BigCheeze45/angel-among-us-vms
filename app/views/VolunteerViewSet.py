from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from app.models.Volunteer import Volunteer
from app.serializer.VolunteerSerializer import VolunteerSerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer

    def retrieve(self, request: Request, pk=None):
        team = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(team)
        return Response(serializer.data)
