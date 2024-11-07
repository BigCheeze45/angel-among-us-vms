from django.utils import timezone

from mysql.connector import MySQLConnection

from mimesis import Field, Gender
from mimesis.random import Random

from common.constants import (
    AAU_TEAMS,
    SHELTER_ID,
    GA_COUNTIES,
    AAU_JOB_TITLES,
    ISHELTERS_CREATED_BY_IDS,
)


# region iShelter loaders
def load_ishelters_desired_job(
    connection: MySQLConnection, random: Random, field: Field
):
    print("Assigning staff to teams")
    cursor = connection.cursor(named_tuple=True)
    cursor.execute("SELECT personId AS person_id FROM staff")
    staff_ids = [row.person_id for row in cursor.fetchall()]

    cursor.execute("SELECT id FROM signInType")
    job_ids = [row.id for row in cursor.fetchall()]

    data = []
    for staff in staff_ids:
        if field("development.boolean"):
            selected_jobs = []
            # randomly assign this staff to multiple teams (jobs)
            for _ in range(field("numeric.integer_number", start=1, end=5)):
                job = random.choice(job_ids)
                # ensure a staff is assigned the same job (team) multiple times
                while job in selected_jobs:
                    job = random.choice(job_ids)
                selected_jobs.append(job)
                data.append((staff, job, random.choice(ISHELTERS_CREATED_BY_IDS)))
        else:
            data.append(
                (staff, random.choice(job_ids), random.choice(ISHELTERS_CREATED_BY_IDS))
            )

    cursor.execute("TRUNCATE TABLE desiredJob")
    cursor.executemany(
        "INSERT INTO desiredJob (staffId, jobId, createdById) VALUES (%s, %s, %s)", data
    )
    cursor.close()
    print(f"{len(data)} rows loaded")


def load_ishelters_staff_job_title(
    connection: MySQLConnection, random: Random, field: Field
):
    print("Assigning staff job titles")
    cursor = connection.cursor(named_tuple=True)
    cursor.execute("SELECT id FROM jobTitle")
    title_ids = [row.id for row in cursor.fetchall()]

    cursor.execute("SELECT personId AS person_id FROM staff")
    staff_ids = [row.person_id for row in cursor.fetchall()]

    data = []
    for staff in staff_ids:
        if field("development.boolean"):
            selected_titles = []
            # randomly assign non-primary titles
            for _ in range(field("numeric.integer_number", start=1, end=4)):
                title = random.choice(title_ids)
                while title in selected_titles:
                    title = random.choice(title_ids)
                selected_titles.append(title)
                data.append(
                    (staff, title, "0", random.choice(ISHELTERS_CREATED_BY_IDS))
                )
            # assign primary title, making sure it hasn't already been assigned
            primary = random.choice(title_ids)
            while primary in selected_titles:
                primary = random.choice(title_ids)
            data.append((staff, primary, "1", random.choice(ISHELTERS_CREATED_BY_IDS)))
        else:
            # Randomly assign a primary title
            # fmt: off
            data.append(
                (staff, random.choice(title_ids), "1", random.choice(ISHELTERS_CREATED_BY_IDS))
            )
            # fmt:on

    cursor.execute("TRUNCATE TABLE staffJobTitle")
    cursor.executemany(
        "INSERT INTO staffJobTitle (staffId, titleId, `primary`, createdById) VALUES (%s, %s, %s, %s)",
        data,
    )
    cursor.close()
    print(f"{len(data)} rows loaded")


def load_ishelters_staff(connection: MySQLConnection, random: Random, field: Field):
    print("Loading staff")
    cursor = connection.cursor(named_tuple=True)
    cursor.execute("SELECT id FROM person")
    data = []
    for person in cursor.fetchall():
        data.append(
            (
                person.id,
                "1" if field("development.boolean") else "0",
                "1" if field("development.boolean") else "0",
                (
                    None
                    if field("development.boolean")
                    else field("datetime.date", start=2013)
                ),
                None if field("development.boolean") else field("text.sentence"),
                None if field("development.boolean") else field("text.sentence"),
                random.choice(ISHELTERS_CREATED_BY_IDS),
            )
        )

    cursor.execute("TRUNCATE TABLE staff")
    cursor.executemany(
        "INSERT INTO staff (personId, current, volunteer, dateJoined, shortBio, longBio, createdById)"
        " VALUES (%s, %s, %s, %s, %s, %s, %s)",
        data,
    )
    cursor.close()
    print(f"{len(data)} rows loaded")


def load_ishelters_person(
    connection: MySQLConnection, random: Random, field: Field, num_person
):
    print("Loading person")
    cursor = connection.cursor(named_tuple=True)
    cursor.execute("SELECT id FROM country")
    county_ids = [row.id for row in cursor.fetchall()]
    now = timezone.now()

    data = []
    for _ in range(num_person):
        # region Person dict
        gender = random.choice_enum_item(Gender)
        person = {
            "firstName": field("person.first_name", gender=gender),
            "middleName": (
                None
                if field("development.boolean")
                else field("person.first_name", gender=gender)
            ),
            "lastName": field("person.last_name", gender=gender),
            "nickName": (
                None
                if field("development.boolean")
                else field("person.first_name", gender=gender)
            ),
            "additionalNames": (
                None
                if field("development.boolean")
                else field("person.first_name", gender=gender)
            ),
            "birthDate": (
                None
                if field("development.boolean")
                else field("person.birthdate", min_year=1965, max_year=2022)
            ),
            "anniversaryDate": (
                None
                if field("development.boolean")
                else field("person.birthdate", min_year=2013)
            ),
            "sexID": random.choice([478, 477, None]),
            "personHousingStatusId": random.choice([739, None]),
            "personHouseInspectionStatusId": random.choice([739, 471, None]),
            "inspectionDate": (
                None
                if field("development.boolean")
                else field("person.birthdate", min_year=2012)
            ),
            "IDTypeId": random.choice([460, None]),
            "heardId": random.choice([918, None]),
            "homePhone": (
                None if field("development.boolean") else field("person.phone_number")
            ),
            "workPhone": (
                None if field("development.boolean") else field("person.phone_number")
            ),
            "cellPhone": field("person.phone_number"),
            "email": field("person.email"),
            "email2": None if field("development.boolean") else field("person.email"),
            "address": field("address.address"),
            "address2": (
                None if field("development.boolean") else field("address.address")
            ),
            "city": field("address.city"),
            "region": random.choice(
                [
                    field("address.state", abbr=field("development.boolean")),
                    "GA",
                    "Georgia",
                    None,
                ]
            ),
            "postalCode": field("address.zip_code"),
            "countryId": random.choice(county_ids),
            "commentsGeneral": (
                None if field("development.boolean") else field("text.sentence")
            ),
            "commentsHidden": (
                None if field("development.boolean") else field("text.sentence")
            ),
            "commentsHousing": (
                None if field("development.boolean") else field("text.sentence")
            ),
            "commentsBanned": (
                None if field("development.boolean") else field("text.sentence")
            ),
            "timeEntered": field("datetime.datetime", timezone=now.tzinfo.tzname(now)),
            "readyToDelete": random.choice(["0", "1"]),
            "shelterId": SHELTER_ID,
            "createdById": random.choice(ISHELTERS_CREATED_BY_IDS),
        }
        # endregion
        data.append(person)
    cols = list(data[0].keys())
    data = [list(item.values()) for item in data]

    vals = "%s, " * len(cols)
    vals = f"{vals[:-2]}"
    stmt = f"INSERT INTO person ({', '.join(cols)}) VALUES ({vals})"
    cursor.executemany(stmt, data)
    cursor.close()
    print(f"{len(data)} rows loaded")


def load_ishelters_sign_in_type(connection: MySQLConnection, random: Random):
    print("Loading AAU Teams")
    cursor = connection.cursor(named_tuple=True)
    cursor.execute("SELECT COUNT(*) AS count FROM signInType")
    row = cursor.fetchone()
    if row.count:
        print("Table already contains data. Same data will not be loaded twice.")
        return

    data = []
    for category, teams in AAU_TEAMS.items():
        for team in teams:
            data.append(
                (
                    f"{category}: {team['name']}",
                    team["description"],
                    SHELTER_ID,
                    "0",
                    random.choice(ISHELTERS_CREATED_BY_IDS),
                )
            )

    stmt = "INSERT INTO signInType (`type`, description, shelterId, `default`, createdById) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(stmt, data)
    cursor.close()
    print(f"{len(data)} rows loaded")


def load_ishelters_job_title(connection: MySQLConnection, random: Random):
    print("Loading AAU job titles")
    cursor = connection.cursor(named_tuple=True)
    cursor.execute("SELECT COUNT(*) AS count FROM jobTitle")
    row = cursor.fetchone()
    if row.count:
        print("Table already contains data. Same data will not be loaded twice.")
        return

    titles = []
    for title in AAU_JOB_TITLES:
        titles.append((title, SHELTER_ID, "0", random.choice(ISHELTERS_CREATED_BY_IDS)))

    stmt = "INSERT INTO jobTitle (title, shelterId, `default`, createdById) VALUES (%s, %s, %s, %s)"
    cursor.executemany(stmt, titles)
    cursor.close()
    print(f"{len(titles)} rows loaded")


def load_ishelters_country(connection: MySQLConnection, random: Random):
    print("Loading GA counties")
    cursor = connection.cursor(named_tuple=True)
    cursor.execute("SELECT COUNT(*) AS count FROM country")
    row = cursor.fetchone()
    if row.count:
        # table is not empty. Do not load same data twice
        print("Table already contains data. Same data will not be loaded twice.")
        return

    # region Counties
    counties = []
    for county in GA_COUNTIES:
        counties.append(
            (county, SHELTER_ID, "0", random.choice(ISHELTERS_CREATED_BY_IDS))
        )
    # Use backticks to escape the reserved keyword 'default'
    stmt = "INSERT INTO country (country, shelterId, `default`, createdById) VALUES (%s, %s, %s, %s)"
    cursor.executemany(stmt, counties)
    # endregion
    cursor.close()
    print(f"{len(counties)} rows loaded")


# endregion
