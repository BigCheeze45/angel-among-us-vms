from django.db import models


class Team(models.Model):
    """
    A volunteering team
    """

    class Meta:
        constraints = [
            # fmt: off
            # (https://www.postgresql.org/docs/15/release-15.html#id-1.11.6.5.5.3.4)
            # Allow nulls in the email field but don't count null as unique.
            # Only available on Postgres v15+
            # This is to support importing teams from iShelters where teams
            # don't have email
            models.UniqueConstraint(name="email_null_not_unique", fields=["email"], nulls_distinct=True)
            # fmt: on
        ]

    name = models.CharField(max_length=200, unique=True, null=False)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(null=True)
    ishelters_id = models.IntegerField(unique=True, editable=False)
    ishelters_created_dt = models.DateTimeField(null=True, editable=False)
    application_received_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
