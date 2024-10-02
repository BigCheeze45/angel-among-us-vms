from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from app.models.Team import Team
from app.serializer.TeamSerializer import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
