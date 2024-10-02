from django.contrib import admin


from app.models import (
    Team,
    County,
    Address,
    Volunteer,
    TeamCategory,
    SkillCategory,
    VolunteerTeam,
    VolunteerSkill,
    VolunteerActivity,
    VolunteerMilestone,
)

# make models available in django admin
admin.site.register(Team)
admin.site.register(County)
admin.site.register(Address)
admin.site.register(Volunteer)
admin.site.register(TeamCategory)
admin.site.register(SkillCategory)
admin.site.register(VolunteerTeam)
admin.site.register(VolunteerSkill)
admin.site.register(VolunteerActivity)
admin.site.register(VolunteerMilestone)
