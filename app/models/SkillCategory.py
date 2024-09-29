from django.db import models


class SkillCategory(models.Model):

    category = models.CharField(
        max_length=100, null=False, help_text="e.g. photographer, builder, IT"
    )
    description = models.TextField(
        blank=True, help_text="Brief description of the category"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        help_text="Timestamp when the category was created",
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="Timestamp when the category was last updated"
    )

    def __str__(self):
        return self.category
