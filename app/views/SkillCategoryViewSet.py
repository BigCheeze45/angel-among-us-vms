from django.shortcuts import get_object_or_404
from django.db.models.deletion import ProtectedError

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException, ErrorDetail

from common.constants import ERROR_DETAIL_CODES
from app.models.SkillCategory import SkillCategory
from app.serializer.SkillCategorySerializer import SkillCategorySerializer


class SkillCategoryViewSet(ModelViewSet):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer

    def retrieve(self, request: Request, pk=None):
        team = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(team)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            detail = ErrorDetail(
                f"Cannot delete this category because it is still in use",
                code=ERROR_DETAIL_CODES.get("ProtectedError"),
            )
            exception = APIException(detail=detail)
            return Response(
                exception=True,
                status=status.HTTP_409_CONFLICT,
                data=exception.get_full_details(),
            )
