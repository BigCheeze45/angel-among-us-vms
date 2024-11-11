from django.db import models

from app.models.Volunteer import Volunteer


class VolunteerPet(models.Model):
    """
    Association table linking Volunteers and the pets they have.
    """
    volunteer = models.ForeignKey(
        Volunteer, on_delete=models.CASCADE, related_name="pet"
    )
    
    description = models.TextField(
        blank=True, null=True, help_text="Detailed description of the Volunteer Pet"
    )
    
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description
