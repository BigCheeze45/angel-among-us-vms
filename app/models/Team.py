from django.db import models

from app.models.TeamCategory import TeamCategory


class Team(models.Model):
    """
    A volunteering team
    """

    email = models.EmailField(null=False, db_column="team_email")
    last_modified_at = models.DateField(null=True, auto_now=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    description = models.TextField(null=True, db_column="team_description")
    name = models.CharField(null=False, db_column="team_name", max_length=100)
    category = models.ForeignKey(
        TeamCategory,
        db_column="category_id",
        # Raise an error when trying to delete a category
        # associated with a team
        on_delete=models.PROTECT,
    )

    # Info imported from iShelters
    ishelters_id = models.IntegerField(null=True, editable=False)
    ishelters_created_dt = models.DateTimeField(null=True, editable=False)
    # TODO - make this a FK relationship to Users.ishelters_id
    ishelters_created_by_id = models.IntegerField(null=True, editable=False)
    application_received_date = models.DateTimeField(null=True, editable=False)

    def __str__(self) -> str:
        return self.name
