# Configuration
These are the available options that can be set and made available
to the docker container.

Note that after changing your `.env`, you must run `make restart` to
apply the new changes.

```ini
# region REQUIRED
# These options are required and must be set
# for the containers & application to initialize/start correctly.
# Uncomment them (remove #) and set an appropriate value

# You can use https://djecrety.ir to generate a key
# SECRET_KEY=

# SECURITY WARNING: don't run with debug turned on in production!
# Importantly, this controls how CORS requests/headers are handled.
# https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
DEBUG=True

# Application database configuration
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_PORT=5432
POSTGRES_HOST=host.docker.internal
POSTGRES_DATABASE=aau_vms

# React-Admin frontend
# Only VITE_SOME_KEY will be exposed as import.meta.env.VITE_SOME_KEY
# to the client source code. This is to prevent accidentally
# leaking env variables to the client
VITE_GOOGLE_CLIENT_ID=

# Email configuration
# This configures what to use when sending email. Defaults to Gmail SMTP
# but note there are limitations (https://support.google.com/a/answer/176600?hl=en - Option 2)
# You may need to create an app password:
# https://support.google.com/accounts/answer/185833?hl=en
# If you choose not to configure email or don't want the ETL
# report email, set this to False
ETL_EMAIL_REPORT=True
# EMAIL_USER must be a complete email address (e.g. myemail@gmail.com)
EMAIL_USER=
EMAIL_PASSWORD=

# ETL CONFIGURATION
# The following options configure how the ETL
# script connects to & operate on iShelters data
# Alternatively, configuration can be done via a
# JSON file that's loaded into the django container.
# See example_etl_config.jsonc. Not that if, available,
# a config file takes precedence over environment variables
# All options listed at the link below are supported
# but you need to prefix them with ISHELTERS (e.g. ISHELTERS_AUTOCOMMIT)
# https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html

# iShelters source configuration
ISHELTERS_USERNAME=
ISHELTERS_PASSWORD=
ISHELTERS_PORT=3306
ISHELTERS_HOST=host.docker.internal
ISHELTERS_AUTOCOMMIT=True
ISHELTERS_DATABASE=aau_ishelters
# endregion

# region OPTIONAL
# These setting are optional with the following defaults

# If you set DEBUG to False, you also need to properly set the ALLOWED_HOSTS setting.
# This should be comma separated hosts
# https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-ALLOWED_HOSTS
ALLOWED_HOSTS = *

REQUIRE_AUTH=True

# The port the vite dev server is accessible on outside of the container
# during development (i.e. npm run dev)
VITE_PORT=80
# URL of the django API backend
VITE_JSON_SERVER_URL=http://localhost:${DJANGO_PORT}
VITE_REQUIRE_AUTH=${REQUIRE_AUTH}

# The port Django is accessible on outside of the container
DJANGO_PORT=8000
DJANGO_LOG_LEVEL=INFO

# Global timezone
TZ=America/New_York

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_TIMEOUT=60
# These are mutually exclusive. Only set one of
# them True. If using SSL, set the correct EMAIL_PORT
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
# Including a trailing space so appended text is not squished
EMAIL_SUBJECT_PREFIX="AAU VMS "
DEFAULT_FROM_EMAIL="aauvms@localhost"

# ETL options
# Comma separated email recipients (e.g., "First Last <email>", "<email>")
# Note that no email is sent if ETL_EMAIL_REPORT=False, even
# if you specify recipients
ETL_REPORT_RECIPIENTS=

# When importing volunteers, only import individuals marked
# as active (i.e. ishelters.staff.current = 1)
ETL_ACTIVE_VOLUNTEERS_ONLY=False

# The VMS tracks team assignment with a start and end date.
# When a team assignment is deleted from iShelters, end date
# is updated to show a volunteer is no longer on that team.
# Set this to true to delete team assignments when they're
# deleted in iShelters
ETL_TEAM_ASSIGNMENT_MATCH_SOURCE=False

# See link for more details
# https://github.com/adamchainz/django-cors-headers?tab=readme-ov-file#configuration
# If True, all origins will be allowed. Other settings restricting allowed origins will be ignored
# If not specified, defaults to the value of DEBUG
# CORS_ALLOWED_ORIGINS
# A comma separated list of origins that are authorized to make cross-site HTTP requests
# CORS_ALLOW_ALL_ORIGINS
```