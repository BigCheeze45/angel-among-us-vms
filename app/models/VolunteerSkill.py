from django.db import models
from app.models import Volunteer, SkillCategory


class Volunteer(models.Model):
    name = models.CharField(max_length=100)


class VolunteerSkill(models.Model):
    volunteer = models.ForeignKey(
        Volunteer, on_delete=models.CASCADE, related_name="volunteer_skills"
    )
    category = models.ForeignKey(
        SkillCategory, on_delete=models.CASCADE, related_name="category_skills"
    )
    proficiency_level = models.IntegerField(
        default=0, help_text="Skill proficiency level from 0 to 10"
    )
    years_of_experience = models.DecimalField(
        max_digits=4, decimal_places=1, help_text="Years of experience in this skill"
    )
    verified = models.BooleanField(
        default=False, help_text="Whether the skill has been verified by an admin"
    )
    date_acquired = models.DateField(
        blank=True, null=True, help_text="The date the volunteer acquired the skill"
    )
    description = models.TextField(
        blank=True, null=True, help_text="Detailed description of the skill"
    )
    certificate_url = models.URLField(
        blank=True, null=True, help_text="URL of the skill certificate (if any)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.volunteer} - {self.category} (Proficiency: {self.proficiency_level})"
