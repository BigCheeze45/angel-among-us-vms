from django.db import models
from models.TeamCategory import TeamCategory


class Team(models.Model):
    teamID = models.AutoField(primary_key=True)
    type_id = models.ForeignKey(TeamCategory.TC_id, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    email = models.EmailField(max_length=200)
