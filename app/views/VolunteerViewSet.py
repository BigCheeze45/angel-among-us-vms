
from rest_framework import viewsets

from app.models.Volunteer import Volunteer
from app.serializer.VolunteerSerializer import VolunteerSerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
