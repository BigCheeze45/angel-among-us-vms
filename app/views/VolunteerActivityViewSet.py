from rest_framework import viewsets
from app.models.VolunteerActivity import VolunteerActivity
from app.serializer.VolunteerActivitySerializer import VolunteerActivitySerializer


# ViewSets define the view behavior.
class VolunteerActivityViewSet(viewsets.ModelViewSet):
    queryset = VolunteerActivity.objects.all()
    serializer_class = VolunteerActivitySerializer
