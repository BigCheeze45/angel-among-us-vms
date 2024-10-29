from typing import Any

from django.db import transaction
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from mimesis import Field, Locale
from mimesis.random import Random

from app.models.Team import Team
from app.models.Volunteer import Volunteer
from app.models.VolunteerTeam import VolunteerTeam
from app.models.VolunteerSkill import VolunteerSkill
from app.models.VolunteerActivity import VolunteerActivity
from app.models.VolunteerMilestone import VolunteerMilestone


GA_COUNTIES = [
    "Appling",
    "Atkinson",
    "Bacon",
    "Baker",
    "Baldwin",
    "Banks",
    "Barrow",
    "Bartow",
    "Ben Hill",
    "Berrien",
    "Bibb",
    "Bleckley",
    "Brantley",
    "Brooks",
    "Bryan",
    "Bulloch",
    "Burke",
    "Butts",
    "Calhoun",
    "Camden",
    "Candler",
    "Carroll",
    "Catoosa",
    "Charlton",
    "Chatham",
    "Chattahoochee",
    "Chattooga",
    "Cherokee",
    "Clarke",
    "Clay",
    "Clayton",
    "Clinch",
    "Cobb",
    "Coffee",
    "Colquitt",
    "Columbia",
    "Cook",
    "Coweta",
    "Crawford",
    "Crisp",
    "Dade",
    "Dawson",
    "Decatur",
    "DeKalb",
    "Dodge",
    "Dooly",
    "Dougherty",
    "Douglas",
    "Early",
    "Echols",
    "Effingham",
    "Elbert",
    "Emanuel",
    "Evans",
    "Fannin",
    "Fayette",
    "Floyd",
    "Forsyth",
    "Franklin",
    "Fulton",
    "Gilmer",
    "Glascock",
    "Glynn",
    "Gordon",
    "Grady",
    "Greene",
    "Gwinnett",
    "Habersham",
    "Hall",
    "Hancock",
    "Haralson",
    "Harris",
    "Hart",
    "Heard",
    "Henry",
    "Houston",
    "Irwin",
    "Jackson",
    "Jasper",
    "Jeff",
    "Jefferson",
    "Jenkins",
    "Johnson",
    "Jones",
    "Lamar",
    "Lanier",
    "Laurens",
    "Lee",
    "Liberty",
    "Lincoln",
    "Long",
    "Lowndes",
    "Lumpkin",
    "Macon",
    "Madison",
    "Marion",
    "McDuffie",
    "McIntosh",
    "Meriwether",
    "Miller",
    "Mitchell",
    "Monroe",
    "Montgomery",
    "Morgan",
    "Murray",
    "Muscogee",
    "Newton",
    "Oconee",
    "Oglethorpe",
    "Paulding",
    "Peach",
    "Pickens",
    "Pierce",
    "Pike",
    "Polk",
    "Pulaski",
    "Putnam",
    "Quitman",
    "Rabun",
    "Randolph",
    "Richmond",
    "Rockdale",
    "Schley",
    "Screven",
    "Seminole",
    "Spalding",
    "Stephens",
    "Stewart",
    "Sumter",
    "Talbot",
    "Taliaferro",
    "Tattnall",
    "Taylor",
    "Telfair",
    "Terrell",
    "Thomas",
    "Tift",
    "Toombs",
    "Towns",
    "Treutlen",
    "Troup",
    "Turner",
    "Twiggs",
    "Union",
    "Upson",
    "Walker",
    "Walton",
    "Ware",
    "Warren",
    "Washington",
    "Wayne",
    "Webster",
    "Wheeler",
    "White",
    "Whitfield",
    "Wilcox",
    "Wilkes",
    "Wilkinson",
    "Worth",
]


class Command(BaseCommand):
    help = "Load fake data"
    field = Field(Locale.EN)
    mimesis_random = Random()
    user = None

    def handle(self, *args: Any, **options: Any) -> str | None:
        if not User.objects.filter(username="srogers"):
            self.user = User.objects.create(
                username="srogers", first_name="Steve", last_name="Rogers"
            )
        else:
            self.user = User.objects.get(username="srogers")

        print("Loading Teams")
        self.load_teams()
        print(f"Loaded {Team.objects.count()} teams")

        print("Loading Volunteers")
        self.load_volunteers()
        print(f"Loaded {Volunteer.objects.count()} Volunteers")

        print("Loading Users")
        self.load_users()
        print(f"Loaded {User.objects.count()} users")

        print("Assigning volunteers to teams")
        self.assign_volunteer_to_teams()
        print(f"Assigned {VolunteerTeam.objects.count()} Volunteers")

        print("Assigning milestones to volunteers")
        self.assign_volunteer_milestones()
        print(f"Assigned {VolunteerMilestone.objects.count()} milestones")

        print("Assigning activities to volunteers")
        self.assign_volunteer_activities()
        print(f"Assigned {VolunteerActivity.objects.count()} activities")

        print("Assigning skills to volunteers")
        self.assign_volunteer_skills()
        print(f"Assigned {VolunteerSkill.objects.count()} skills to volunteers")

    def assign_volunteer_skills(self, activities_per_volunteer: int = 3):
        for v in Volunteer.objects.all():
            for _ in range(activities_per_volunteer):
                VolunteerSkill.objects.create(
                    volunteer=v,
                    proficiency_level=self.field(
                        "numeric.integer_number", start=1, end=10
                    ),
                    years_of_experience=self.field(
                        "numeric.integer_number", start=1, end=10
                    ),
                )

    def assign_volunteer_activities(self, activities_per_volunteer: int = 3):
        county = self.mimesis_random.choice(GA_COUNTIES)
        for v in Volunteer.objects.all():
            for _ in range(activities_per_volunteer):
                VolunteerActivity.objects.create(
                    volunteer=v,
                    start_date=self.field(
                        "datetime.date",
                        start=2016,
                        end=2022,
                    ),
                    end_date=self.field(
                        "datetime.date",
                        start=2016,
                        end=2022,
                    ),
                    hours_spent=self.field("numeric.decimal_number", start=10.0),
                    location=county,
                    description=self.field("text.sentence"),
                    status=self.mimesis_random.choice(["ongoing", "completed"]),
                )

    def assign_volunteer_milestones(self, milestones_per_volunteer: int = 3):
        for v in Volunteer.objects.all():
            # assign each volunteer the provided number of milestones
            for _ in range(milestones_per_volunteer):
                rand_bool = self.field("development.boolean")
                VolunteerMilestone.objects.create(
                    volunteer=v,
                    milestone_date=self.field(
                        "datetime.date",
                        start=2016,
                        end=2022,
                    ),
                    years_of_service=self.field(
                        "numeric.integer_number", start=1, end=10
                    ),
                    award_title=self.field("text.color"),
                    award_description=(
                        self.field("text.sentence") if rand_bool else None
                    ),
                    achievement_level=self.mimesis_random.choice(
                        ["bronze", "silver", "gold"]
                    ),
                )

    def load_users(self, num_users: int = 100):
        for _ in range(num_users):
            User.objects.create(
                first_name=self.field("person.first_name"),
                last_name=self.field("person.last_name"),
                username=self.field("person.username", mask="l_l_d"),
                email=self.field("person.email", unique=True),
                date_joined=self.field(
                    "datetime.datetime",
                    start=2016,
                    end=2024,
                ),
                is_active=self.field("development.boolean"),
                is_staff=self.field("development.boolean"),
                is_superuser=self.field("development.boolean"),
            )

    def assign_volunteer_to_teams(self):
        num_teams = Team.objects.count()
        num_volunteers = Volunteer.objects.count()
        team_distribution = self.get_volunteer_distributions(num_teams, num_volunteers)

        start = 0
        volunteers = Volunteer.objects.all().order_by("id")
        for i, team in enumerate(Team.objects.all()):
            team_volunteers = volunteers[start : start + team_distribution[i]]
            for v in team_volunteers:
                VolunteerTeam.objects.create(team=team, volunteer=v)
            print(f"{team.name} assigned {team_distribution[i]} member(s)")
            start += team_distribution[i]

    def load_volunteers(self, num_volunteers: int = 100):
        for _ in range(num_volunteers):
            county = self.mimesis_random.choice(GA_COUNTIES)
            state = self.mimesis_random.choice(["Georgia", "GA"])
            # rand_bool = self.mimesis_random.choice([True, False])
            rand_bool = self.field("development.boolean")

            if rand_bool:
                address_line_2 = (
                    f"Apt. 0{self.field('numeric.integer_number', start=10, end=100)}"
                )
                has_maddie_certifications = True
                maddie_certifications_received_date = self.field(
                    "datetime.date", start=2013
                )
            else:
                address_line_2 = None
                has_maddie_certifications = False
                maddie_certifications_received_date = None

            try:
                Volunteer.objects.create(
                    first_name=self.field("person.first_name"),
                    middle_name=self.field("person.last_name") if rand_bool else None,
                    last_name=self.field("person.last_name"),
                    preferred_name=(
                        self.field("person.first_name") if rand_bool else None
                    ),
                    email=self.field("person.email", unique=True),
                    active_status_change_date=self.field(
                        "datetime.date", start=2016, end=2024
                    ),
                    created_by=self.user,
                    active=self.field("development.boolean"),
                    cell_phone=self.field("person.phone_number"),
                    date_of_birth=self.field("person.birthdate"),
                    has_maddie_certifications=has_maddie_certifications,
                    maddie_certifications_received_date=maddie_certifications_received_date,
                    ishelters_access_flag=self.field("development.boolean"),
                    ishelters_category_type=self.mimesis_random.choice(
                        [
                            "AAU Officer",
                            "AAU Volunteer",
                            "AAU Team Lead",
                            "AAU Board Member",
                            "AAU Staff Member",
                        ]
                    ),
                    ishelters_created_dt=self.field(
                        "datetime.datetime",
                        start=2018,
                        end=2023,
                    ),
                    address_line_1=f"{self.field('address.street_number', maximum=1700)} {self.field('address.street_name')}",
                    address_line_2=address_line_2,
                    county=county,
                    city=self.field("address.city"),
                    state=state,
                    zipcode=self.field("address.zip_code"),
                )
            except IntegrityError:
                continue

        volunteers = Volunteer.objects.select_for_update().all()
        with transaction.atomic():
            for volunteer in volunteers:
                volunteer.date_joined = self.field(
                    "datetime.datetime",
                    start=2018,
                    end=2024,
                )

    def load_teams(self):
        team_categories = {
            "Admin": [
                {
                    "name": "Customer Service",
                    "description": "Includes main phone, email, and joinus",
                    "email": "cs@aau.org",
                },
                {
                    "name": "Customer Service - Assistance Team",
                    "description": None,
                    "email": "csat@aau.org",
                },
                {
                    "name": "Email Administration",
                    "description": None,
                    "email": "email@aau.org",
                },
                {
                    "name": "Finance & Executive Team",
                    "description": None,
                    "email": "fande@aau.org",
                },
                {
                    "name": "Information Technology",
                    "description": None,
                    "email": "it@aau.org",
                },
                {
                    "name": "Ishelters Administration",
                    "description": None,
                    "email": "ishelters@aau.org",
                },
                {
                    "name": "Maddie's Fund Training",
                    "description": None,
                    "email": "maddies@aau.org",
                },
                {"name": "Moves", "description": None, "email": "moves@auu.org"},
                {
                    "name": "PetFinder & Adopt-a-Pet",
                    "description": None,
                    "email": "PetFinder-Adopt-a-Pet@aau.org",
                },
                {"name": "Prayer Team", "description": None, "email": "prayup@aau.org"},
                {"name": "Puppy Team", "description": None},
                {"name": "Vet Records", "description": None},
            ],
            "Apps": [
                {"name": "Volunteers", "description": None},
                {"name": "Foster - Dog", "description": None},
                {"name": "App Uploaders", "description": None},
                {"name": "Adoption - Dog", "description": None},
            ],
            "Cats": [
                {"name": "Cat Records", "description": None},
                {"name": "Cat Vetting", "description": None},
                {"name": "Cat Foster Apps", "description": None},
                {"name": "Cat Adoption Apps", "description": None},
                {"name": "Petco Cat Habitat", "description": None},
            ],
            "Foster Support": [
                {"name": "Boarding Admin", "description": None},
                {"name": "Boarding Buddies", "description": None},
                {"name": "Foster Home Checks", "description": None},
                {"name": "Foster Home Rechecks", "description": None},
                {"name": "Foster Placements", "description": None},
                {"name": "Mentors", "description": None},
                {"name": "Supplies Team", "description": None},
                {"name": "Training", "description": None},
            ],
            "Fundraising": [
                {"name": "Events", "description": None},
                {"name": "Grant Writer", "description": None},
                {"name": "Social Media Team", "description": None},
                {"name": "Donations Support & Acknowledgement", "description": None},
            ],
            "Intakes": [
                {"name": "Intakes Coordinator", "description": None},
                {"name": "Pulls Coordinator", "description": None},
                {"name": "Returns Coordinator", "description": None},
                {"name": "Shelter Liaison", "description": None},
                {"name": "Temperament Tests", "description": None},
                {"name": "Transport Coordinators", "description": None},
                {"name": "Transporter", "description": None},
            ],
            "Outreach": [
                {"name": "Education and Community Outreach", "description": None},
            ],
            "Vet": [
                {"name": "Heartworm Team", "description": None},
                {"name": "Intake Vetting", "description": None},
                {"name": "Pharmacy", "description": None},
                {"name": "Prevents", "description": None},
                {"name": "Spay/Neuter Team", "description": None},
                {"name": "Vet Cases", "description": None},
                {"name": "Vet Team", "description": None},
            ],
        }

        for category_name, teams in team_categories.items():
            for team in teams:
                if "email" not in team:
                    email = "".join("_" if not c.isalpha() else c for c in team["name"])
                    email = f"{email}@aau.org".lower()
                    team["email"] = email

                Team.objects.create(**team)

    @classmethod
    def get_volunteer_distributions(cls, num_teams, num_volunteers):
        """Returns this list of integers, where each integer represents the final number of volunteers for a team"""
        if num_volunteers < num_teams:
            raise CommandError(
                "Not enough volunteers to assign at least one to each team"
            )

        # Ensure each team gets at least one volunteer
        base_distribution = 1
        remaining_volunteers = num_volunteers - num_teams

        # Calculate additional volunteers per team
        additional_per_team = remaining_volunteers // num_teams
        extra_volunteers = remaining_volunteers % num_teams

        # Create the distribution list
        distribution = [base_distribution + additional_per_team] * num_teams

        # Distribute the extra volunteers
        for i in range(extra_volunteers):
            distribution[i] += 1

        return distribution
