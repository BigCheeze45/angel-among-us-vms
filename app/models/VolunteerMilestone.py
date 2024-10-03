from django.db import models

from app.models.Volunteer import Volunteer


class VolunteerMilestone(models.Model):
    volunteer = models.ForeignKey(
        Volunteer, on_delete=models.CASCADE, related_name="milestones"
    )
    milestone_date = models.DateField(null=False)
    years_of_service = models.IntegerField(default=0)
    award_title = models.CharField(max_length=100, null=True, blank=True)
    award_description = models.TextField(null=True, blank=True)
    achievement_level = models.CharField(
        max_length=10,
        choices=[("bronze", "Bronze"), ("silver", "Silver"), ("gold", "Gold")],
        default="bronze",
    )

    def __str__(self):
        return f"Milestone for {self.volunteer.full_name}: {self.years_of_service} years"
