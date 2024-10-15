from typing import Any

from django.core.management.base import BaseCommand

import mysql.connector

class Command(BaseCommand):
    help = "Synchronize VMS with iShelters"

    def handle(self, *args: Any, **options: Any) -> str | None:
        # https://dev.mysql.com/doc/connector-python/en/
        cnx = mysql.connector.connect(
            user=None,
            password=None,
            host=None,
            database=None,
        )
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM person")
        for row in cursor:
            print(row)

        # close connection to iShelters
        cursor.close()
        cnx.close()
