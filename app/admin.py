from django.contrib import admin

from app.models.Team import Team
from app.models.Volunteer import Volunteer
from app.models.TeamCategory import TeamCategory
from app.models.VolunteerTeam import VolunteerTeam

# make models available in django admin
admin.site.register(Team)
admin.site.register(Volunteer)
admin.site.register(TeamCategory)
admin.site.register(VolunteerTeam)
