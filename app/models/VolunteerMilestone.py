from django.db import models
from django.contrib.auth.models import User


class VolunteerMilestone(models.Model):
    volunteer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="milestones"
    )
    milestone_date = models.DateField(null=False)
    years_of_service = models.IntegerField(default=0)
    award_description = models.TextField(null=True, blank=True)
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
