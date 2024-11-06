from rest_framework import serializers

from app.models.Volunteer import Volunteer
from app.models.VolunteerTeam import VolunteerTeam
from app.models.VolunteerSkill import VolunteerSkill
from app.models.VolunteerActivity import VolunteerActivity
from app.models.VolunteerPet import VolunteerPet
from app.models.VolunteerChildren import VolunteerChildren

from app.serializer.VolunteerSkillSerializer import VolunteerSkillSerializer
from app.serializer.VolunteerActivitySerializer import VolunteerActivitySerializer
from app.serializer.VolunteerChildrenSerializer import VolunteerChildrenSerializer
from app.serializer.VolunteerPetSerializer import VolunteerPetSerializer


class TeamWithStartDateSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="team.id")
    name = serializers.CharField(source="team.name")
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()


class VolunteerSerializer(serializers.ModelSerializer):
    teams = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()
    activities = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    pet = serializers.SerializerMethodField()

    class Meta:
        model = Volunteer
        # include all fields except the following
        exclude = ["ishelters_created_dt"]

    def get_skills(self, obj):
        volunteer_skills = VolunteerSkill.objects.filter(volunteer=obj).select_related(
            "volunteer"
        )
        return VolunteerSkillSerializer(volunteer_skills, many=True).data

    def get_activities(self, obj):
        volunteer_activities = VolunteerActivity.objects.filter(
            volunteer=obj
        ).select_related("volunteer")
        return VolunteerActivitySerializer(volunteer_activities, many=True).data

    def get_teams(self, obj):
        volunteer_teams = VolunteerTeam.objects.filter(volunteer=obj).select_related(
            "team"
        )
        return TeamWithStartDateSerializer(volunteer_teams, many=True).data
    def get_children(self,obj):
        volunteer_children = VolunteerChildren.objects.filter(volunteer=obj).select_related(
            "volunteer"
        )
        return VolunteerChildrenSerializer(volunteer_children, many=True).data

    def get_pet(self,obj):
        volunteer_pet = VolunteerPet.objects.filter(volunteer=obj).select_related(
            "volunteer"
        )
        return VolunteerPetSerializer(volunteer_pet, many=True).data

    

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
