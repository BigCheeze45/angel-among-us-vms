from django.contrib.auth.models import User

from rest_framework import viewsets

from app.serializer.UserSerializer import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
