from django.db import models

from app.models.Volunteer import Volunteer

class VolunteerActivity(models.Model):
    volunteer = models.ForeignKey(
        Volunteer, on_delete=models.CASCADE, related_name="activities"
    )
    end_date = models.DateField(null=True)
    activity_name = models.CharField(max_length=200)
    start_date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    hours_spent = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=[("ongoing", "Ongoing"), ("completed", "Completed")],
        default="ongoing",
    )

    def __str__(self):
        return f"{self.activity_name} by {self.volunteer.first_name}"
