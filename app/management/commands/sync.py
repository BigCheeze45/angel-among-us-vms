import pprint
from typing import Any
from pathlib import Path

from django.conf import settings
from django.utils import timezone
from django.forms.models import model_to_dict
from django.db.utils import Error as DjangoDbError
from django.core.management.base import BaseCommand

import pyjson5

from mysql.connector import MySQLConnection
from mysql import connector as mysql_connector
from mysql.connector.errors import Error as MySqlError

from app.models.Team import Team
from app.models.Volunteer import Volunteer
from app.models.VolunteerTeam import VolunteerTeam


# https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/
class Command(BaseCommand):
    requires_migrations_checks = True
    requires_system_checks = ["__all__"]
    help = "Synchronize VMS with iShelters"

    def handle(self, *args: Any, **options: Any) -> str | None:
        # Attempt to load ETL configuration
        self._load_config(options)

        source_connection_info = options.get("source_database")
        # Test connection & exit
        if options.get("test_connection"):
            success = self._test_connection(source_connection_info)
            if not success:
                exit(1)

            exit(0)

        # Test connection & exit if not successful
        success = self._test_connection(source_connection_info)
        if not success:
            exit(1)

        # https://dev.mysql.com/doc/connector-python/en/
        cnx = mysql_connector.connect(**source_connection_info)

        # region ETL/migration
        # 1: Update team membership
        delete_assignments = options.get("team_assignment_match_source")
        membership_results = self._update_team_assignments(
            cnx, delete_assignments=delete_assignments
        )
        if delete_assignments:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{membership_results[0]} team assignments deleted because"
                    " they do not exist in iShelters"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Updated end_date on {membership_results} volunteer/team assignments"
                )
            )

        # 2: Update & load new teams
        team_results = self._load_teams(cnx)
        for key, value in team_results.items():
            self.stdout.write(f"{len(value)} {key}")

        # 3: Update & load new volunteers
        active_volunteers_only = options.get("active_volunteers_only")
        volunteer_results = self._load_volunteers(
            cnx, active_volunteers_only=active_volunteers_only
        )
        for key, value in volunteer_results.items():
            self.stdout.write(f"{len(value)} {key}")

        # 4: Load new team assignments
        vt_results = self._load_team_assignments(cnx)
        for key, value in vt_results.items():
            self.stdout.write(f"{len(value)} {key}")
        # endregion

        # 5: Generate report
        # TODO

        # 6: Email report
        # TODO

    def add_arguments(self, parser):
        parser.add_argument(
            # Read configuration file from cli. Assume config.jsonc if not provided
            "-c",
            "--config",
            type=Path,
            dest="config_file",
            default=Path("config.jsonc"),
            help="Path to ETL configuration file."
            " Defaults to config.jsonc in the current working directory",
        )

        parser.add_argument(
            "--test-connection",
            default=False,
            action="store_true",
            help="Test connection to the source database then exit",
        )

        return super().add_arguments(parser)

    def _update_team_assignments(
        self, connection: MySQLConnection, delete_assignments=False
    ):
        """
        This function updates volunteer/team relationships by checking
        if an existing V/T relationship is still exists in iShelters' desiredJob
        table. If it does, then the V/T relationship is still considered active
        and nothing happens (i.e relationship is ongoing).

        If the relationship does not exist in iShelter, then `end_date` on
        V/T is updated to indicate the relationship has ended (i.e volunteer
        stopped being a part of that team). Set `delete_assignments` to True
        to delete them instead of setting `end_date`.
        """
        try:
            self.stdout.write(self.style.HTTP_INFO("Updating team assignments"))
            # 1: fetch existing V/T relationships from iShelters
            vt_ishelters_id = tuple(
                # only select V/T that are still active (i.e. end_date is not set)
                VolunteerTeam.objects.filter(end_date__isnull=True)
                .values_list("ishelters_id", flat=True)
                .all()
            )
            if not vt_ishelters_id:
                # no V/T relationships
                return

            cursor = connection.cursor(dictionary=True)
            cursor.execute(f"SELECT id FROM desiredJob WHERE id IN\n{vt_ishelters_id}")
            # of the existing V/T relationships, these are still in iShelters
            ishelters_assignments = [row["id"] for row in cursor.fetchall()]

            # 2: Update end_date for relationships no longer in iShelters
            vt_relationships = (
                VolunteerTeam.objects
                # exclude active relationships
                .exclude(ishelters_id__in=ishelters_assignments)
                # select relationships that don't have an end_date
                .filter(end_date__isnull=True).all()
            )

            if delete_assignments:
                # number of objects deleted and a dictionary with the number of deletions per object type
                # e.g. (5, {'blog.Blog': 1, 'blog.Entry': 2, 'blog.Entry_authors': 2})
                results = vt_relationships.delete()
                return results
            else:
                # Perform a bulk update on all affected objects
                for relationship in vt_relationships:
                    relationship.end_date = timezone.now()
                num_changed = VolunteerTeam.objects.bulk_update(
                    vt_relationships, fields=["end_date"]
                )
                return num_changed
        except DjangoDbError as e:
            self.stderr.write(e)
        except MySqlError as e:
            self.stderr.write(e.msg)
        # finally:
        cursor.close()

    def _load_team_assignments(self, connection: MySQLConnection):
        cursor = connection.cursor(dictionary=True)
        volunteer_ishelters_ids = tuple(
            Volunteer.objects.values_list("ishelters_id", flat=True).all()
        )
        # region Query to extract data from the desiredJob table
        cursor.execute(
            f"""
            SELECT
                jobId AS team,
                id AS ishelters_id,
                staffId AS volunteer,
                timeCreated AS start_date
            FROM desiredJob
            WHERE
                -- select only assignments for imported volunteers
                -- this is better than SELECT * & walking over
                -- thousands of rows that might not be relevant
                staffId IN {volunteer_ishelters_ids}
            """
        )
        # endregion

        inserts = []
        failures = []
        self.stdout.write(self.style.HTTP_INFO("Importing team assignments"))
        rows = cursor.fetchall()
        for row in rows:
            try:
                ishelters_id = row["ishelters_id"]
                # make naive datetime timezone aware
                for dt_field in ["start_date"]:
                    row[dt_field] = timezone.make_aware(row[dt_field])

                # check if this team assignment already exist & skip it
                vt_relationship = VolunteerTeam.objects.filter(
                    ishelters_id=ishelters_id
                ).first()
                if vt_relationship:
                    continue  # skip row & go to next one

                team = Team.objects.filter(ishelters_id=row["team"]).first()
                if team:
                    volunteer = Volunteer.objects.filter(
                        ishelters_id=row["volunteer"]
                    ).first()
                    row["team"] = team
                    row["volunteer"] = volunteer
                    vt = VolunteerTeam.objects.create(**row)
                    self.stdout.write(
                        f"New team assignment {ishelters_id} ({volunteer.full_name} - {team.name}) created"
                    )
                    inserts.append(
                        {
                            "VMS ID": vt.id,
                            "team": vt.team.name,
                            "iShelters ID": vt.ishelters_id,
                            "volunteer": vt.volunteer.full_name,
                        }
                    )
                else:
                    err = f"Cannot import team assignment because iShelters team {row['team']} does not exists"
                    self.stderr.write(err)
                    failures.append({"id": ishelters_id, "error": err})
            except DjangoDbError as e:
                error_slug, error_detail = e.args[0].split("\n")
                error_slug = error_slug.strip()
                error_detail = error_detail.strip()
                self.stderr.write(f"Cannot import assignment: - {error_slug}")
                failures.append({"id": ishelters_id, "error": str(e)})
                continue
            except Exception as e:
                self.stderr.write(f"Unexpected error. Cannot import assignment: {e}")
                failures.append({"id": ishelters_id, "error": str(e)})
                continue
            finally:
                cursor.close()

        return {
            "inserts": inserts,
            "failures": failures,
        }

    def _load_teams(self, connection: MySQLConnection):
        team_failures = []
        team_new_inserts = []
        team_updated_records = []

        cursor = connection.cursor(dictionary=True)
        # region Query to extract data from the signInType table
        cursor.execute(
            """
            SELECT
                id AS ishelters_id,
                type AS name,
                description,
                timeCreated AS ishelters_created_dt
            FROM signInType
            WHERE
                -- Ignore skills
                type NOT LIKE '%Skill:%'
            """
        )
        # endregion
        self.stdout.write(self.style.HTTP_INFO("Importing teams"))
        rows = cursor.fetchall()
        for row in rows:
            try:
                ishelters_id = row["ishelters_id"]
                # make naive datetime objects into timezone aware
                for dt_field in ["ishelters_created_dt"]:
                    row[dt_field] = timezone.make_aware(row[dt_field])

                team = Team.objects.filter(ishelters_id=ishelters_id).first()
                if team:
                    self.stdout.write(
                        f"Team {ishelters_id} ({team.name})"
                        f" record updated on {team.application_received_date}."
                        " Checking for new changes."
                    )

                    team_dict = model_to_dict(
                        team, exclude=["id", "application_received_date", "email"]
                    )
                    team_dict["ishelters_id"] = team.ishelters_id
                    team_dict["ishelters_created_dt"] = team.ishelters_created_dt
                    if row != team_dict:
                        self.stdout.write(
                            self.style.NOTICE("Change in record detected")
                        )
                        # self.stdout.write(f"iShelters Row: {row}")
                        # self.stdout.write(f"VMS Row: {team_dict}")
                        Team.objects.filter(ishelters_id=ishelters_id).update(**row)
                        team = Team.objects.filter(ishelters_id=ishelters_id).first()
                        team_updated_records.append(
                            {
                                "VMS ID": team.id,
                                "email": team.email,
                                "name": team.name,
                                "iShelters ID": team.ishelters_id,
                            }
                        )
                else:
                    team = Team.objects.create(**row)
                    self.stdout.write(
                        f"New team {team.ishelters_id} ({team.name}) created"
                    )
                    team_new_inserts.append(
                        {
                            "VMS ID": team.id,
                            "email": team.email,
                            "name": team.name,
                            "iShelters ID": team.ishelters_id,
                        }
                    )
            except DjangoDbError as e:
                error_slug, error_detail = e.args[0].split("\n")
                error_slug = error_slug.strip()
                error_detail = error_detail.strip()
                self.stderr.write(f"Cannot import {row["name"]} - {error_slug}")
                team_failures.append({"id": ishelters_id, "error": str(e)})
                continue
            except Exception as e:
                self.stderr.write(
                    f"Unexpected error. Cannot import {row["name"]} - {e}"
                )
                team_failures.append({"id": ishelters_id, "error": str(e)})
                continue
            finally:
                cursor.close()

        return {
            "failures": team_failures,
            "inserts": team_new_inserts,
            "updates": team_updated_records,
        }

    def _load_volunteers(
        self, connection: MySQLConnection, active_volunteers_only=False
    ):
        # To access rows by column names
        cursor = connection.cursor(dictionary=True)

        # region Query to extract data from the person table
        base_volunteer_query = """
            SELECT
                -- Use column alias to match Django model field names
                p.id AS ishelters_id,
                firstName AS first_name,
                lastName AS last_name,
                middleName AS middle_name,
                CONCAT(
                    firstName,
                    ' ',
                    IFNULL(CONCAT(middleName, ' '), ''),
                    lastName
                ) AS full_name,
                nickName AS preferred_name,
                jt.title AS job_title,
                birthDate AS date_of_birth,
                s.dateJoined AS date_joined,
                email,
                s.current AS active,
                p.timeCreated AS ishelters_created_dt,
                cellPhone AS cell_phone,
                homePhone AS home_phone,
                workPhone AS work_phone,
                address AS address_line_1,
                address2 AS address_line_2,
                city,
                country AS county,
                region AS state,
                postalCode AS zipcode
            FROM
                person p
                -- join staff to get current (active) & dateJoined
                JOIN staff s ON p.id = s.personId
                -- join staffJobTitle to find their job assignments
                JOIN staffJobTitle sjt ON s.personId = sjt.staffId
                -- join jobTitle to get the actual title name
                JOIN jobTitle jt ON sjt.titleId = jt.id
                /* LEFT JOIN country to get county, including persons
                with no county */
                LEFT JOIN country c ON p.countryId = c.id
            WHERE
                -- select only volunteers
                volunteer = '1'
                -- select just the primary job
                AND sjt.primary = '1'
            """
        # endregion

        if active_volunteers_only:
            base_volunteer_query += "\nANDs.current = '1'"
        base_volunteer_query += ";"

        volunteer_new_inserts = []
        volunteer_updated_records = []
        volunteer_failures = []

        self.stdout.write(self.style.HTTP_INFO("Importing volunteers"))
        cursor.execute(base_volunteer_query)
        rows = cursor.fetchall()  # fetch all rows
        for row in rows:
            try:
                ishelter_id = row["ishelters_id"]
                # make naive datetime objects into timezone aware
                for dt_field in [
                    "date_joined",
                    "date_of_birth",
                    "ishelters_created_dt",
                ]:
                    if row[dt_field]:
                        row[dt_field] = timezone.make_aware(row[dt_field])

                volunteer = Volunteer.objects.filter(ishelters_id=ishelter_id).first()
                # region Existing volunteer
                if volunteer:
                    self.stdout.write(
                        f"Volunteer {ishelter_id} ({volunteer.full_name})"
                        f" record updated on {volunteer.application_received_date}."
                        " Checking for new changes."
                    )

                    # turn instance into a dictionary for easy comparison
                    volunteer_dict = model_to_dict(
                        volunteer,
                        exclude=[
                            "id",
                            "application_received_date",
                            "has_maddie_certifications",
                            "active_status_change_date",
                            "maddie_certifications_received_date",
                        ],
                    )
                    # tweak the dict to match row types
                    volunteer_dict["active"] = "1" if volunteer_dict["active"] else "0"

                    # fmt: off
                    # these are not editable as defined in the model so they're
                    # automatically excluded from the dict. This adds them back in
                    volunteer_dict["ishelters_id"] = volunteer.ishelters_id
                    volunteer_dict["ishelters_created_dt"] = volunteer.ishelters_created_dt
                    # fmt: on

                    if row != volunteer_dict:
                        self.stdout.write(self.style.NOTICE("Change found in detected"))
                        # self.stdout.write(f"iShelters Row: {row}")
                        # self.stdout.write(f"VMS Row: {volunteer_dict}")

                        if row["active"] != volunteer_dict["active"]:
                            # active status has changed
                            row["active_status_change_date"] = timezone.now()

                        # https://docs.djangoproject.com/en/5.1/ref/models/querysets/#django.db.models.query.QuerySet.update
                        # update volunteer by passing in the iShelters row, matching on ishelters_id
                        Volunteer.objects.filter(ishelters_id=ishelter_id).update(**row)

                        # select updated record
                        volunteer = Volunteer.objects.filter(
                            ishelters_id=ishelter_id
                        ).first()
                        volunteer_updated_records.append(
                            {
                                "VMS ID": volunteer.id,
                                "email": volunteer.email,
                                "name": volunteer.full_name,
                                "iShelters ID": volunteer.ishelters_id,
                            }
                        )
                    # endregion
                else:
                    # region New volunteer
                    volunteer = Volunteer.objects.create(**row)
                    self.stdout.write(
                        f"New volunteer {volunteer.ishelters_id} ({volunteer.full_name}) created"
                    )
                    volunteer_new_inserts.append(
                        {
                            "VMS ID": volunteer.id,
                            "email": volunteer.email,
                            "name": volunteer.full_name,
                            "iShelters ID": volunteer.ishelters_id,
                        }
                    )
                    # endregion
            except DjangoDbError as e:
                error_slug, error_detail = e.args[0].split("\n")
                error_slug = error_slug.strip()
                error_detail = error_detail.strip()
                self.stderr.write(f"Cannot import {row["full_name"]}: {error_slug}")
                # mark it as a failure
                volunteer_failures.append({"id": ishelter_id, "error": str(e)})
                continue  # go to next row
            except Exception as e:
                self.stderr.write(
                    f"Unexpected error. Cannot import {row["full_name"]}: {e}"
                )
                volunteer_failures.append({"id": ishelter_id, "error": str(e)})
                continue
            finally:
                cursor.close()

        return {
            "failures": volunteer_failures,
            "inserts": volunteer_new_inserts,
            "updates": volunteer_updated_records,
        }

    def _test_connection(self, connection_info: dict) -> bool:
        success = False
        if not connection_info:
            self.stderr.write(
                f"Source connection information is None. Unable to continue."
            )
            return success

        try:
            mysql_connector.connect(**connection_info)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully connected to {connection_info['host']} using provided credentials"
                )
            )
            success = True
        except MySqlError as e:
            self.stderr.write(e.msg)
        except Exception as e:
            self.stderr.write(f"Unexpected error:{e}\n")

        return success

    def _load_config(self, options: dict):
        """Load migration configuration into `options`"""
        # 1: is config file provided?
        config_file: Path = options.get("config_file")
        if not config_file:
            self.stderr.write(
                (
                    "Migration configuration file not provided."
                    " Provide a valid JSON or .JSONC configuration file."
                    "\nBy default, the current working directory is checked for 'config.jsonc'."
                    "\nIf this is running inside of a container, verify the file is properly mounted."
                    "\nMigration process will now exit."
                )
            )
            exit(1)

        # 2: does the provided config file exists
        if not config_file.exists():
            self.stderr.write(
                (
                    f"{str(config_file.absolute())} not found."
                    "\nDoes this file exists?"
                    " Verify the path then try again."
                    "\nMigration process will now exit."
                )
            )
            exit(1)

        # 3: is the provided config file valid
        try:
            with open(config_file) as input_:
                config = pyjson5.load(input_)
        except pyjson5.Json5DecoderException as e:
            self.stderr.write(
                (
                    f"Failed parsing {str(config_file.absolute())}."
                    "\nMake sure the file is valid JSON or JSONC."
                    "\nMigration process will now exit."
                )
            )
            self.stderr.write(f"{e.message}")
            exit(1)

        # Check email settings
        if "email" not in config:
            self.stdout.write(
                self.style.WARNING(
                    "Email configuration not provided. Falling back to Django settings."
                )
            )
        email = {
            "host": settings.EMAIL_HOST,
            "port": settings.EMAIL_PORT,
            "user": settings.EMAIL_HOST_USER,
            "use_ssl": settings.EMAIL_USE_SSL,
            "use_tls": settings.EMAIL_USE_TLS,
            "password": settings.EMAIL_HOST_PASSWORD,
        }
        config.update(email=email)
        try:
            if "time_zone" not in config["source_database"]:
                self.stdout.write(
                    self.style.WARNING(
                        "Source database timezone not provided. Falling back to Django settings."
                    )
                )
                config["source_database"].update(time_zone=settings.TIME_ZONE)
        except KeyError:
            pass

        self.stdout.write(self.style.SUCCESS("Configuration file loaded"))
        self.stdout.write(pprint.pformat(config))

        # Load configuration into options
        options.update(**config)
