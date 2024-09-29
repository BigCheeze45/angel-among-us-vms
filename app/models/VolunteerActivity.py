from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Volunteer(models.Model):
    name = models.CharField(max_length=100)


class VolunteerActivity(models.Model):
    volunteer = models.ForeignKey(
        Volunteer, on_delete=models.CASCADE, related_name="activities"
    )
    activity_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
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
        return f"{self.activity_name} by {self.volunteer.name}"
