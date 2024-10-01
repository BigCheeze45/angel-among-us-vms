from rest_framework import viewsets
from app.models.VolunteerMilestone import VolunteerMilestone
from app.serializer import VolunteerMilestoneSerializer


class VolunteerMilestoneViewSet(viewsets.ModelViewSet):
    queryset = VolunteerMilestone.objects.all()
    serializer_class = VolunteerMilestoneSerializer
