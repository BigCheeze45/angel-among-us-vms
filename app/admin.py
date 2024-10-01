from django.contrib import admin


from app.models import (
    Team,
    TeamCategory,
    SkillCategory,
    VolunteerTeam,
    VolunteerSkill,
    VolunteerActivity,
)

# make models available in django admin
admin.site.register(Team)
admin.site.register(TeamCategory)
admin.site.register(SkillCategory)
admin.site.register(VolunteerTeam)
admin.site.register(VolunteerSkill)
admin.site.register(VolunteerActivity)
