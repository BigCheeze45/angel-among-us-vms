from django.db import models


class TeamCategory(models.Model):
    """
    Overarching category to group teams by
    """

    name = models.CharField(null=False, max_length=200, unique=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    last_modified_at = models.DateTimeField(null=True, auto_now=True)

    # Info imported from iShelters
    ishelters_id = models.IntegerField(null=True, editable=False)
    ishelters_created_dt = models.DateTimeField(null=True, editable=False)
    # TODO - make this a FK relationship to Users.ishelters_id
    ishelters_created_by_id = models.IntegerField(null=True, editable=False)
    application_received_date = models.DateTimeField(null=True, editable=False)

    def __str__(self) -> str:
        return self.name
