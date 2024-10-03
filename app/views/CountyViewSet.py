from rest_framework import viewsets

from app.models.County import County
from app.serializer.CountySerializer import CountySerializer


class CountyViewSet(viewsets.ModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer
