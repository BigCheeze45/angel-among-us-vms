from rest_framework import viewsets

from app.serializer import VolunteerMilestoneSerializer
from app.models.VolunteerMilestone import VolunteerMilestone


class VolunteerMilestoneViewSet(viewsets.ModelViewSet):
    queryset = VolunteerMilestone.objects.all()
    serializer_class = VolunteerMilestoneSerializer
