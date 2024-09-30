from django.contrib import admin


from app.models import (
    TeamCategory,
    VolunteerTeam,
)

# make models available in django admin
admin.site.register(TeamCategory)
admin.site.register(VolunteerTeam)
