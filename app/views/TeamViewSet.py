from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from app.models.Team import Team
from app.serializer.TeamSerializer import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def retrieve(self, request: Request, pk=None):
        team = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(team)
        return Response(serializer.data)
