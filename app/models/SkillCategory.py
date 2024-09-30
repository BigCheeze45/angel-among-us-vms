from django.db import models


class SkillCategory(models.Model):
    """
    Category to group skills by
    """

    category = models.CharField(
        max_length=100, null=False, unique=True, help_text="e.g. Photographer, builder, IT"
    )
    description = models.TextField(
        blank=True, help_text="Brief description of the category"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the category was created",
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="Timestamp when the category was last updated"
    )

    def __str__(self):
        return self.category
