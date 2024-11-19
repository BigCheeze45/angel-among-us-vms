# Migration/ETL Script
The ETL/migration script leverages Django admin command to make
it easy to configure and run. As noted below, configuration can be done via a
config file (JSON/JSONC) or provided as environment variables. In either case,
these need to be set _inside_ of the Django container.

## Triggering a migration
Once the configuration has been set, you can trigger a migration in a couple of ways:

* Outside of the container: use `make sync` [target](make.md)
* Inside the container: `./manage.py sync` OR `make sync`

Check the [usage docs](#sync-usage) for available options

## Configuration
Any of the connection arguments listed [here](https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html)
can be provided when setting up the connection to iShelters.

Note that if providing the arguments via environment variables, you must prefix them with `ISHELTERS`
for it to be parsed correctly.

### Environment Variable
```ini
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
## iShelters source configuration
ISHELTERS_USERNAME=
ISHELTERS_PASSWORD=
ISHELTERS_PORT=3306
ISHELTERS_HOST=host.docker.internal
ISHELTERS_AUTOCOMMIT=True
ISHELTERS_DATABASE=aau_ishelters

## ETL options
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
```

### Config JSON
```json
{
    /*
        Connection information for the source (i.e. iShelters) database.
        This is passed directly to the mysql connector and all options
        listed at the link below are supported:
        https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
    */
    "source_database": {
        "username": null,
        "password": null,
        "database": null,
        "host": null
        // Default to Django time zone if not provided
        // "time_zone": "America/New_York"
    },
    /*
        Individuals to be notified when the ETL is complete.
        They will receive a report of changes
    */
    "report_recipients": [],
    /*
        When importing volunteers, only import
        individuals marked as active (i.e. 
        ishelters.staff.current = 1)
    */
    "active_volunteers_only": false,
    /*
        The VMS tracks team assignment with a start and end date.
        When a team assignment is deleted from iShelters, end date
        is updated to show a volunteer is no longer on that team.
        Set this to true to delete team assignments when they're deleted
        in iShelters
    */
    "team_assignment_match_source": false,
    /*
        If you choose not to configure email or don't want the ETL
        report email, set this to false
    */
    "email_report": true
}
```
## Sync usage
```text
usage: manage.py sync [-h] [-c CONFIG_FILE] [--test-connection]

Synchronize VMS with iShelters

options:
  -h, --help            show this help message and exit
  -c, --config CONFIG_FILE
                        Path to ETL configuration file
  --test-connection     Test connection to the source database then exit
```
