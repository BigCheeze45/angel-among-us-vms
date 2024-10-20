from django.contrib import admin


from app.models import (
    Team,
    Volunteer,
    VolunteerTeam,
    VolunteerSkill,
    VolunteerActivity,
)

# make models available in django admin
admin.site.register(Team)
admin.site.register(Volunteer)
admin.site.register(VolunteerTeam)
admin.site.register(VolunteerSkill)
admin.site.register(VolunteerActivity)
