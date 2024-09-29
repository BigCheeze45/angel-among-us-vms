from rest_framework import viewsets
from app.models import VolunteerSkill
from app.serializers import VolunteerSkillSerializer


class VolunteerSkillViewSet(viewsets.ModelViewSet):
    queryset = VolunteerSkill.objects.all()
    serializer_class = VolunteerSkillSerializer
