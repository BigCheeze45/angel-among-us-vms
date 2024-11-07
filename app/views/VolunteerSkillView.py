from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.request import Request
from rest_framework.response import Response
from app.models.Volunteer import Volunteer
from app.models.VolunteerSkill import VolunteerSkill
from app.serializer.VolunteerSkillSerializer import VolunteerSkillSerializer


class VolunteerSkillViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerSkillSerializer

    def create(self, request, *args, **kwargs):
        # DONE - check if uer has permission to add skill to a volunteer
        if not request.user.has_perm("app.add_volunteerskill"):
            raise PermissionDenied(
                "You do not have permission to add a skill to this volunteer."
            )
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # DONE - check if a user has permissions to delete a volunteer's skill
        if not request.user.has_perm("app.delete_volunteerskill"):
            raise PermissionDenied(
                "You do not have permission to delete this volunteer's skill."
            )
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        queryset = VolunteerSkill.objects.all()

        volunteer_id = self.kwargs.get("volunteer_pk")
        if volunteer_id:
            volunteer = get_object_or_404(Volunteer, id=volunteer_id)
            queryset = queryset.filter(volunteer=volunteer)

        # Apply ordering, order by ID if not specified
        ordering = self.request.query_params.get("ordering", "id")
        queryset = queryset.order_by(ordering)

        return queryset

    def retrieve(self, request: Request, pk=None, *args, **kwargs):
        team = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(team)
        return Response(serializer.data)
