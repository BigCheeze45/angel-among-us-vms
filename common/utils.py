import re
from collections import namedtuple
from pathlib import Path

from django.db.utils import Error

from rest_framework.fields import BooleanField


def convert_string_bool(str_bool: str) -> bool:
    return str_bool.lower() in BooleanField.TRUE_VALUES


ParsedError = namedtuple("ParsedError", ["raw", "slug", "detail", "field"])


def django_db_error_parser(error: Error) -> ParsedError | None:
    column_name_regex = r"Key \((.*?)\)="
    try:
        slug, detail = error.args[0].split("\n")
        slug = slug.strip()
        detail = detail.split("DETAIL:")[1].strip()
    except ValueError:
        return

    # return the parsed error
    column = re.search(column_name_regex, detail).group(1)
    return ParsedError(raw=error, slug=slug, detail=detail, field=column)


def read_docker_secrets_file(secret: str, path: str = "/run/secrets") -> str | None:
    """
    Read the specified secrets file

    :params secrete: Name of secrete file
    :params path: Path to secret file if not in the standard location
    """
    try:
        file_path = Path(path).joinpath(secret)
        with open(file_path) as f:
            return f.readline()
    except FileNotFoundError:
        return None
