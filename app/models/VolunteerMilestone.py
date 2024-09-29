from django.db import models
from django.utils import timezone
from app.models import Volunteer


class Volunteer(models.Model):
    name = models.CharField(max_length=100)


class VolunteerMilestone(models.Model):
    volunteer = models.ForeignKey(
        Volunteer, on_delete=models.CASCADE, related_name="milestones"
    )
    years_of_service = models.IntegerField(default=0)
    milestone_date = models.DateField(default=timezone.now)
    award_title = models.CharField(max_length=100, null=True, blank=True)
    award_description = models.TextField(null=True, blank=True)
    achievement_level = models.CharField(
        max_length=50,
        choices=[("bronze", "Bronze"), ("silver", "Silver"), ("gold", "Gold")],
        default="bronze",
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Milestone for {self.volunteer.name}: {self.years_of_service} years"
