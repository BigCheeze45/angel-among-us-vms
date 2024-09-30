from django.db import models
from django.core.validators import RegexValidator


class Volunteer(models.Model):
    volunteerID = models.AutoField(primary_key=True)
    ishelters_id = models.IntegerField(max_length=10, unique=True)
    address_id = models.ForeignKey(Address.addressID, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    preferred_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)  # Should we make this unique?
    status_change_date = models.DateField()
    created_at = models.DateField(auto_now=True)
    date_joined = models.DateField()
    secondary_email = models.EmailField(max_length=254)
    active = models.BooleanField(default=True)
    home_phone = models.CharField(
        max_length=15,
        validators=RegexValidator(
            regex=r"^-+?1?-d{9,15}$",
            message="Phone numbers must be entered in the format: '999-999-9999'. Up to 15 digits allowed.",
        ),
    )
    cell_phone = models.CharField(
        max_length=15,
        validators=RegexValidator(
            regex=r"^-+?1?-d{9,15}$",
            message="Phone numbers must be entered in the format: '999-999-9999'. Up to 15 digits allowed.",
        ),
    )
    work_phone = models.CharField(
        max_length=15,
        validators=RegexValidator(
            regex=r"^-+?1?-d{9,15}$",
            message="Phone numbers must be entered in the format: '999-999-9999'. Up to 15 digits allowed.",
        ),
    )
    date_of_birth = models.DateField()
    ishelter_profile = models.CharField(max_length=200)
    created_by = models.ForeignKey(User.userID, on_delete=models.CASCADE)
