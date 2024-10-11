from django.db import models

from app.models.County import County


class Address(models.Model):
    """
    A volunteer's address
    """

    address_line_1 = models.CharField(max_length=100, null=False)
    address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=False)
    county = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    zipcode = models.CharField(max_length=10, null=False)

    def __str__(self) -> str:
        if self.address_line_2:
            return f"{self.address_line_1} {self.address_line_2} {self.city} {self.state}, {self.zipcode}"
        else:
            return f"{self.address_line_1} {self.city} {self.state}, {self.zipcode}"
