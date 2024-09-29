from django.db import models


class Volunteer(models.Model):

    name = models.CharField(max_length=10)
