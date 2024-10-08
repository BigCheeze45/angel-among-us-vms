from django.shortcuts import get_object_or_404

from django.db.models.deletion import ProtectedError

from rest_framework import status
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import APIException, ErrorDetail

from app.models.TeamCategory import TeamCategory
from app.serializer.TeamCategorySerializer import TeamCategorySerializer


class TeamCategoryViewSet(viewsets.ModelViewSet):
    queryset = TeamCategory.objects.all()
    serializer_class = TeamCategorySerializer

    def retrieve(self, request: Request, pk=None):
        team = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(team)
        return Response(serializer.data)

    def destroy(self, request, pk, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            detail = ErrorDetail(
                f"Cannot delete this category because it is still in use",
                code="PROTECTED",
            )
            exception = APIException(detail=detail)
            return Response(
                exception=True,
                status=status.HTTP_409_CONFLICT,
                data=exception.get_full_details(),
            )
