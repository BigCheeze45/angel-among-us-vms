from typing import Any
from pathlib import Path

import pyjson5
import mysql.connector
from django.core.management.base import BaseCommand

from mimesis import Field, Locale
from mimesis.random import Random

from common.utils import get_etl_config_from_env
from app.management.commands.common import (
    load_ishelters_staff,
    load_ishelters_person,
    load_ishelters_country,
    load_ishelters_job_title,
    load_ishelters_desired_job,
    load_ishelters_sign_in_type,
    load_ishelters_staff_job_title,
)


class Command(BaseCommand):
    help = "Load fake data generated using mimesis into development iShelters database"
    field = Field(Locale.EN)
    mimesis_random = Random()

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
            "-N",
            "--num-person",
            type=int,
            default=1000,
            help="Number of individuals to load in the 'person' table",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        if options.get("config_file").exists():
            self.stdout.write(
                self.style.WARNING(
                    f"Configuration file found. {options.get('config_file')}"
                )
            )
            with open(options.get("config_file")) as input_:
                config = pyjson5.load(input_)
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Configuration file not found. Attempting to read ETL configuration from environment."
                )
            )
            config = get_etl_config_from_env()
        options.update(**config)

        self._load_ishelters(options)

    def _load_ishelters(self, options):
        self.stdout.write("Generating and loading random data into iShelters")
        conn = mysql.connector.connect(**options.get("source_database"))
        # fyi - order here matters. Later loads depend on prior ones
        # (e.g country needs to load to have IDs available for person)
        load_ishelters_country(conn, self.mimesis_random)
        load_ishelters_job_title(conn, self.mimesis_random)
        load_ishelters_sign_in_type(conn, self.mimesis_random)
        load_ishelters_person(
            conn, self.mimesis_random, self.field, options.get("num_person")
        )
        load_ishelters_staff(conn, self.mimesis_random, self.field)
        load_ishelters_staff_job_title(conn, self.mimesis_random, self.field)
        load_ishelters_desired_job(conn, self.mimesis_random, self.field)

        conn.close()
