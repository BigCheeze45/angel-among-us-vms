from rest_framework import viewsets

from app.models.Team import Team
from app.serializer.TeamSerializer import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    search_fields = [
        "name",
        "email",
        "ishelters_id",
        "description",
    ]

    def get_queryset(self):
        queryset = Team.objects.all()

        # team_id = self.kwargs.get("team_pk")
        # if team_id:
        #     self.serializer_class = VolunteerSerializer
        #     # Get the volunteers associated with the specified team
        #     volunteer_ids = VolunteerTeam.objects.filter(team_id=team_id).values_list(
        #         "volunteer_id", flat=True
        #     )
        #     queryset = Volunteer.objects.filter(id__in=volunteer_ids)

        # apply ordering, order by ID if not specified
        ordering = self.request.query_params.get("ordering", "id")
        queryset = queryset.order_by(ordering)

        return queryset
