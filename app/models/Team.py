from django.db import models


class Team(models.Model):
    """
    A volunteering team
    """

    name = models.CharField(max_length=200, unique=True, null=False)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(null=False, unique=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)

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
