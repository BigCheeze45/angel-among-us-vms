from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from app.models.Address import Address


class Volunteer(models.Model):
    """
    A Volunteer
    """

    first_name = models.CharField(max_length=50, null=False)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=False)
    preferred_name = models.CharField(max_length=50, null=True, blank=True)
    full_name = models.CharField(max_length=155, blank=True)  # First + Middle + Last
    email = models.EmailField(unique=True, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    active_status_change_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)
    cell_phone = PhoneNumberField(max_length=15)
    home_phone = PhoneNumberField(null=True, blank=True, max_length=15)
    work_phone = PhoneNumberField(null=True, blank=True, max_length=15)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.ForeignKey(
        Address, null=True, db_column="address_id", on_delete=models.CASCADE
    )
    ishelters_category_type = models.CharField(null=True)
    ishelters_access_flag = models.BooleanField(null=True)
    ishelters_id = models.IntegerField(null=True, unique=True, editable=False)
    maddie_certifications_received_date = models.DateField(null=True, blank=True)
    has_maddie_certifications = models.BooleanField(default=False)
    ishelters_created_dt = models.DateTimeField(null=True, editable=False)
    application_received_date = models.DateField(null=True, editable=False)
    # ishelters_created_by_id = models.ForeignKey(null=True, editable=False, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs) -> None:
        if not self.full_name:
            # Full is not set so default to concatting individual names
            if self.middle_name:
                self.full_name = f"{self.first_name.strip()} {self.middle_name.strip()} {self.last_name.strip()}"
            else:
                self.full_name = f"{self.first_name.strip()} {self.last_name.strip()}"
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.full_name
