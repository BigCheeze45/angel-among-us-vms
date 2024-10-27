from rest_framework import viewsets
from app.models.Volunteer import Volunteer
from app.models.VolunteerTeam import VolunteerTeam
from app.serializer.VolunteerSerializer import VolunteerSerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerSerializer

    filterset_fields = [
        "active",
        "ishelters_access_flag",
        "ishelters_category_type",
        "has_maddie_certifications",
        "maddie_certifications_received_date",
    ]
    search_fields = [
        "full_name",
        "preferred_name",
    ]

    def get_queryset(self):
        queryset = Volunteer.objects.all()

        team_id = self.request.query_params.get("team_id")
        if team_id:
            # return only volunteers on this team
            volunteer_ids = VolunteerTeam.objects.filter(team_id=team_id).values_list(
                "volunteer_id", flat=True
            )
            queryset = queryset.filter(id__in=volunteer_ids)

        county = self.request.query_params.get("county")
        if county:
            if county.lower() == "undefined":
                # return volunteers with no address on file
                queryset = Volunteer.objects.filter(
                    county=""
                ) | Volunteer.objects.filter(county__isnull=True)
            else:
                # return volunteers based on their county
                queryset = queryset.filter(county=county)

        # apply ordering, order by ID if not specified
        ordering = self.request.query_params.get("ordering", "id")
        queryset = queryset.order_by(ordering)

        return queryset
