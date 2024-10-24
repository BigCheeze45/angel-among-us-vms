from typing import Any

from django.core.management.base import BaseCommand

import mysql.connector

import django

from app.models.Team import Team
from app.models.Volunteer import Volunteer
from app.models.TeamCategory import TeamCategory
from app.models.SkillCategory import SkillCategory
from app.models.VolunteerTeam import VolunteerTeam
from app.models.VolunteerSkill import VolunteerSkill
from app.models.VolunteerActivity import VolunteerActivity
from app.models.VolunteerMilestone import VolunteerMilestone


class Command(BaseCommand):
    help = "Synchronize VMS with iShelters"

    def handle(self, *args: Any, **options: Any) -> str | None:
        # https://dev.mysql.com/doc/connector-python/en/

        cursor = None
        try:

            cnx = mysql.connector.connect(
                user="root",
                password="Tootsie054052",
                # Connect to ishelters container
                host="aau_ishelters",
                database="aau_ishelters",
            )
            cursor = cnx.cursor()
            # To access rows by column names
            cursor = cnx.cursor(dictionary=True)
            # Query to extract data from the person table
            cursor.execute(
                "SELECT person.*, staff.dateJoined, staff.current, staff.personID, staff.volunteer FROM person INNER JOIN staff ON staff.personId = person.id;"
            )

            rows = cursor.fetchall()  # fetch all rows

            volunteer_new_inserts = []
            volunteer_updated_records = []
            volunteer_failures = []

            for row in rows:
                try:
                    # extract individual fields from each row
                    ishelter_id = row["id"]
                    f_name = row["firstName"]
                    m_name = row["middleName"]
                    l_name = row["lastName"]
                    preferred_name = row["nickName"]
                    full_name = f"{f_name} {m_name} {l_name}".strip()
                    birth_date = row["birthDate"]
                    date_joined = row["dateJoined"]
                    email = row["email"]
                    # No active field in the ishelters
                    # active = row["active"]
                    created_at = row["timeCreated"]
                    # created_by = row["createdById"]
                    cell_phone = row["cellPhone"]
                    home_phone = row["homePhone"]
                    work_phone = row["workPhone"]
                    address = row["address"]
                    address2 = row["address2"]
                    city = row["city"]
                    county = row["county"]
                    state = row["region"]
                    zipcode = row["postalCode"]
                    time_created = row["timeCreated"]
                    current = row["current"]

                    volunteer = (
                        Volunteer.objects.using("default")
                        .filter(ishelters_id=ishelter_id)
                        .first()
                    )

                    if volunteer:
                        # Update if any fields have changed
                        updated = False
                        if volunteer.ishelters_id != ishelter_id:
                            volunteer.ishelters_id = ishelter_id
                            updated = True
                        if volunteer.first_name != f_name:
                            volunteer.first_name = f_name
                            updated = True
                        if volunteer.middle_name != m_name:
                            volunteer.middle_name = m_name
                            updated = True
                        if volunteer.last_name != l_name:
                            volunteer.last_name = l_name
                            updated = True
                        if volunteer.preferred_name != preferred_name:
                            volunteer.preferred_name = preferred_name
                            updated = True
                        if volunteer.full_name != full_name:
                            volunteer.full_name = full_name
                            updated = True
                        if volunteer.date_of_birth != birth_date:
                            volunteer.date_of_birth = birth_date
                            updated = True
                        if volunteer.date_joined != date_joined:
                            volunteer.date_joined = date_joined
                            updated = True
                        if volunteer.email != email:
                            volunteer.email = email
                            updated = True
                        if volunteer.created_at != created_at:
                            volunteer.created_at = created_at
                            updated = True
                        if volunteer.cell_phone != cell_phone:
                            volunteer.cell_phone = cell_phone
                            updated = True
                        if volunteer.home_phone != home_phone:
                            volunteer.home_phone = home_phone
                            updated = True
                        if volunteer.active != current:
                            volunteer.active = current
                            updated = True
                        if volunteer.work_phone != work_phone:
                            volunteer.work_phone = work_phone
                            updated = True
                        if volunteer.address_line_1 != address:
                            volunteer.address_line_1 = address
                            updated = True
                        if volunteer.address_line_2 != address2:
                            volunteer.address_line_2 = address2
                            updated = True
                        if volunteer.city != city:
                            volunteer.city = city
                            updated = True
                        if volunteer.county != county:
                            volunteer.county = county
                            updated = True
                        if volunteer.state != state:
                            volunteer.state = state
                            updated = True
                        if volunteer.zipcode != zipcode:
                            volunteer.zipcode = zipcode
                            updated = True
                        if volunteer.ishelters_created_dt != time_created:
                            volunteer.ishelters_created_dt = time_created
                            updated = True

                        if updated:
                            volunteer.save(using="default")
                            volunteer_updated_records.append(
                                {
                                    "id": volunteer.id,
                                    "first_name": volunteer.first_name,
                                    "last_name": volunteer.last_name,
                                    "email": volunteer.email,
                                }
                            )
                    else:
                        # Insert new record
                        record = Volunteer(
                            first_name=f_name,
                            middle_name=m_name,
                            last_name=l_name,
                            preferred_name=preferred_name,
                            full_name=full_name,
                            email=email,
                            date_joined=date_joined,
                            created_at=created_at,
                            active=current,
                            cell_phone=cell_phone,
                            home_phone=home_phone,
                            work_phone=work_phone,
                            date_of_birth=birth_date,
                            address_line_1=address,
                            address_line_2=address2,
                            city=city,
                            county=county,
                            state=state,
                            zipcode=zipcode,
                            ishelters_id=ishelter_id,
                            ishelters_created_dt=time_created,
                        )
                        record.save()

                        volunteer_new_inserts.append(
                            {
                                "first_name": record.first_name,
                                "last_name": record.last_name,
                                "email": record.email,
                            }
                        )

                except django.db.utils.IntegrityError as IE:
                    volunteer_failures.append({"id": ishelter_id, "error": str(IE)})

            # Query to extract data from the signInType table
            cursor.execute("SELECT * FROM signInType")

            rows = cursor.fetchall()  # fetch all rows

            team_new_inserts = []
            team_updated_records = []
            team_failures = []

            for row in rows:
                try:
                    team_name = row["type"]
                    ishelters_id = row["id"]
                    time_created2 = row["timeCreated"]
                    description = row["description"]
                    created_by_id = row["createdById"]

                    vms_team = (
                        Team.objects.using("default")
                        .filter(ishelters_id=ishelters_id)
                        .first()
                    )

                    if vms_team:
                        updated = False
                        if vms_team.ishelters_id != ishelters_id:
                            vms_team.ishelters_id = ishelters_id
                            updated = True
                        if vms_team.description != description:
                            vms_team.description = description
                            updated = True
                        if vms_team.ishelters_created_dt != time_created2:
                            vms_team.ishelters_created_dt = time_created2
                            updated = True
                        if vms_team.name != team_name:
                            vms_team.name = team_name
                            updated = True
                        if vms_team.ishelters_created_by_id != created_by_id:
                            vms_team.ishelters_created_by_id = created_by_id
                            updated = True

                        if updated:
                            vms_team.save(using="default")
                            team_updated_records.append(
                                {
                                    "name": vms_team.name,
                                    "description": vms_team.description,
                                    "ishelters_id": vms_team.ishelters_id,
                                }
                            )
                    else:
                        # insert new record
                        team_record = Team(
                            ishelters_id=ishelters_id,
                            name=team_name,
                            description=description,
                            ishelters_created_dt=time_created2,
                            ishelters_created_by_id=created_by_id,
                        )
                        team_record.save()

                        team_new_inserts.append(
                            {
                                "first_name": record.first_name,
                                "last_name": record.last_name,
                                "email": record.email,
                            }
                        )
                except django.db.utils.IntegrityError as IE:
                    team_failures.append({"id": ishelters_id, "error": str(IE)})

            # Query to extract data from the desireJob table
            cursor.execute("SELECT * FROM desiredJob")

            rows = cursor.fetchall()  # fetch all rows

            vt_new_inserts = []
            vt_updated_records = []
            vt_failures = []

            for row in rows:
                try:
                    ishelter_id = row["id"]
                    staff_id = row["staffId"]
                    job_id = row["jobId"]
                    time_created_3 = row["timeCreated"]

                    vms_vt = (
                        VolunteerTeam.objects.using("default")
                        .filter(id=ishelter_id)
                        .first()
                    )

                    if vms_vt:
                        updated = False
                        if vms_vt.team != job_id:
                            vms_vt.team = job_id
                            updated = True
                        if vms_vt.volunteer != staff_id:
                            vms_vt.volunteer = staff_id
                            updated = True
                        if vms_vt.created_at != time_created_3:
                            vms_vt.created_at = time_created_3
                            updated = True

                        vt_updated_records.append(
                            {
                                "team": job_id,
                                "volunteer": staff_id,
                                "ishelter_id": ishelter_id,
                            }
                        )
                    else:
                        vt_record = VolunteerTeam(
                            team=job_id,
                            volunteer=staff_id,
                            created_at=time_created_3,
                            id=ishelter_id,
                        )

                        vt_record.save()
                        vt_new_inserts.append(
                            {
                                "team": vt_record.team,
                                "volunteer": vt_record.volunteer,
                                "ishelter_id": vt_record.id,
                            }
                        )

                except django.db.utils.IntegrityError as IE:
                    vt_failures.append({"id": ishelter_id, "error": str(IE)})
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            # close connection to iShelters
            if cursor:  # Ensure cursor is closed only if it was initialized
                cursor.close()
            if cnx:  # Ensure connection is closed
                cnx.close()
