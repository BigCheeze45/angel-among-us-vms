from django.db import models


class Volunteer(models.Model):
    """
    A Volunteer
    """

    first_name = models.CharField(max_length=50, null=False)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=False)
    preferred_name = models.CharField(max_length=100, null=True, blank=True)
    full_name = models.CharField(max_length=155, blank=True)  # First + Middle + Last
    email = models.EmailField(unique=True, null=False)
    date_joined = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    cell_phone = models.CharField(max_length=128)
    home_phone = models.CharField(null=True, blank=True, max_length=128)
    work_phone = models.CharField(null=True, blank=True, max_length=128)
    date_of_birth = models.DateField(blank=True, null=True)

    job_title = models.CharField(null=True, default="AAU Volunteer")
    ishelters_id = models.IntegerField(unique=True, editable=False)
    maddie_certifications_received_date = models.DateField(null=True, blank=True)
    ishelters_created_dt = models.DateTimeField(null=True, editable=False)
    application_received_date = models.DateTimeField(auto_now=True)

    # A volunteer's address
    address_line_1 = models.CharField(max_length=100, null=False)
    address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=False)
    county = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=False)
    zipcode = models.CharField(max_length=10, null=False)

    def save(self, *args, **kwargs) -> None:
        if not self.full_name:
            # Full is not set so default to concatenating individual names
            if self.middle_name:
                self.full_name = f"{self.first_name.strip()} {self.middle_name.strip()} {self.last_name.strip()}"
            else:
                self.full_name = f"{self.first_name.strip()} {self.last_name.strip()}"
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.full_name
