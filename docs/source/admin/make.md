# Makefile and targets
For convenience a [makefile](<https://en.wikipedia.org/wiki/Make_(software)>) is included with this project
to streamline a number of repetitive tasks. A helpful explanation and tutorial
of Make is available [here](https://makefiletutorial.com).

Executing a make command looks like this:

`make target`

where `target` is any target specified in the makefile.

Assuming you have `make` (or are inside the dev container), you can run any of
the targets listed below. Note that some targets (e.g., `sync, super, migrate`)
are executed _inside_ the Django container and will raise an error when
it is not running.

| **Target**     | **Description**                                                                                         | Context |
|----------------|---------------------------------------------------------------------------------------------------------|---------|
| init           | Spin up the development environment. This is the default target if one is not provided (e.g. `make`)    | local   |
| build          | Build application docker images                                                                         | local   |
| up             | Bring up the application docker compose stack (start the app)                                           | local   |
| down           | Bring down the application docker compose stop (stop the app)                                           | local   |
| restart        | Stop then restart the stack                                                                             | local   |
| login          | Log into the specified container e.g. `make login container=django`                                     | local   |
| clean          | Stop the app and remove volumes and other build files. Effectively start from scratch at the next `up`. | local   |
| cleaninit      | Combine `clean + init`. Effectively start from scratch at the next `up`.                                | local   |
| cleanishelters | Destroy and rebuild the iShelters dev database (MySQL)                                                  | local   |
| cleanvms       | Destroy and rebuild the application database (PostgreSQL)                                               | local   |
| cleandbs       | Combine cleaning the vms & ishelters. Effectively start from scratch at the next `up`.                  | local   |
| makemigrations | creates new migration files based on the changes detected in the models                                 | Django  |
| migrate        | Synchronize change made to models with the schema in the database                                       | Django  |
| mimesis        | Load fake data generated using mimesis into development iShelters database                              | Django  |
| sync           | Synchronize iShelters with VMS (i.e., copy volunteer data from iShelters to VMS)                        | Django  |
| super          | Create a new Django admin super user                                                                    | Django  |

_Generated using [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables#)_

## Using makefile on Windows

Windows does not support make files natively. However, if you have installed/enabled WSL,
you can open a WSL terminal to use the makefile.
