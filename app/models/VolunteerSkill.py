from django.db import models

from app.models.Volunteer import Volunteer


class VolunteerSkill(models.Model):
    """
    Association table linking Volunteers and the skills/interests they have.
    """

    type = models.CharField(max_length=10, null=False)
    skill = models.CharField(max_length=100, null=False)
    volunteer = models.ForeignKey(
        Volunteer,
        db_column="volunteer_id",
        on_delete=models.CASCADE,
        related_name="skills",
    )

    def __str__(self):
        return self.skill
