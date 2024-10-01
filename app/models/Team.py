from django.db import models

from app.models.TeamCategory import TeamCategory


class Team(models.Model):
    """
    A volunteering team
    """

    name = models.CharField(max_length=200, unique=True, null=False)
    description = models.TextField(blank=True)
    email = models.EmailField(null=False, unique=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
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
    application_received_date = models.DateTimeField(null=True, editable=False)
    # TODO - make this a FK relationship to Users.ishelters_id
    ishelters_created_by_id = models.IntegerField(
        null=True, editable=False
    )  # , on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name
