from django.contrib import admin

from app.models.Team import Team
from app.models.Volunteer import Volunteer
from app.models.TeamCategory import TeamCategory

admin.site.register(Team)
admin.site.register(Volunteer)
admin.site.register(TeamCategory)
