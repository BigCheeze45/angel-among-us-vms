from django.db import models

from app.models.Team import Team
from app.models.Volunteer import Volunteer


class VolunteerTeam(models.Model):
    """
    Association table linking Volunteers and the teams they're on.

    Once a Volunteer has been assigned a team, that relationship is
    permanent. Neither the volunteer or team can be changed. Instead,
    a new relationship should be created.
    """

    team = models.ForeignKey(
        Team,
        # editable=False,
        db_column="team_id",
        # when a team is deleted, also delete all its members
        on_delete=models.CASCADE,
    )
    volunteer = models.ForeignKey(
        Volunteer,
        editable=False,
        db_column="volunteer_id",
        # when a Volunteer is deleted, also delete their team membership
        on_delete=models.CASCADE,
    )
    end_date = models.DateTimeField(null=True, blank=True)
    last_modified_at = models.DateField(null=True, auto_now=True)
    start_date = models.DateTimeField(null=False, auto_now_add=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self) -> str:
        # cheap hack for admin view
        return f"{self.volunteer.full_name} => {self.team.name}"
