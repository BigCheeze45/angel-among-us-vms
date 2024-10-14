from django.db import models

from app.models.Volunteer import Volunteer
from app.models.SkillCategory import SkillCategory


class VolunteerSkill(models.Model):
    """
    Association table linking Volunteers and the skills they have.
    """

    # skill = models.CharField(max_length=100, null=True)
    volunteer = models.ForeignKey(
        Volunteer,
        db_column="volunteer_id",
        on_delete=models.CASCADE,
        related_name="skills",
    )
    category = models.ForeignKey(
        SkillCategory,
        db_column="category_id",
        # Raise an error when trying to delete a category
        # associated with a skill
        on_delete=models.PROTECT,
    )
    proficiency_level = models.IntegerField(
        default=1, help_text="Skill proficiency level from 0 to 10"
    )
    years_of_experience = models.DecimalField(
        max_digits=4, decimal_places=1, help_text="Years of experience in this skill"
    )
    description = models.TextField(
        blank=True, null=True, help_text="Detailed description of the skill"
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.volunteer} - {self.category} (Proficiency: {self.proficiency_level})"
