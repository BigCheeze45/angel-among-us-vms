from django.db import models

from app.models.Volunteer import Volunteer


class VolunteerActivity(models.Model):
    volunteer = models.ForeignKey(
        Volunteer, on_delete=models.CASCADE, related_name="activities"
    )
    start_date = models.DateField(null=False)
    description = models.TextField(null=True, blank=True)
    activity_name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.activity_name
