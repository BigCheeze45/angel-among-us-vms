from django.db import models


class County(models.Model):
    """
    The County an address belong in
    """

    name = models.CharField(max_length=100, null=False, unique=True)
    ishelters_id = models.IntegerField(null=True, unique=True, editable=False)

    def __str__(self) -> str:
        return self.name
