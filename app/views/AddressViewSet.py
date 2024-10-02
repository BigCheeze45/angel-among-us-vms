from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from app.models.Address import Address
from app.models.Volunteer import Volunteer
from app.serializer.AddressSerializer import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
