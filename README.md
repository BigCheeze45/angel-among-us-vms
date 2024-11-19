# Angel Among Us Volunteer Management System

Volunteer management system using a Django REST backend (via [Django REST framework
](https://www.django-rest-framework.org))
with a React (via [React-Admin](https://marmelab.com/react-admin/)) frontend.

# Documentation
Project docs are available in the [docs](./docs/) folder.

# Getting Started

**Instructions and setup below are for development and should not be used when deploying
to production.**

## Perquisites

To get the project up and running, you'll need:

- [Docker](https://www.docker.com)

  - If installing on Windows, you may need to install/enable [WSL-2](https://learn.microsoft.com/en-us/windows/wsl/install) first.

- You IDE of choice
- Some familiarity with terminal/command prompt

  - If using Windows, it's recommended to install & use [Windows Terminal](https://learn.microsoft.com/en-us/windows/terminal/install).

## Running It

### Environment file

First things first is to create your environment file. This file defines
environment variables that are accessible from any process.

1. In the project folder, create a file named `.env` (note the dot in the file name)
2. Edit `.env` by setting the required options

```plaintext
# Minimal .env - Check example.env and docker-compose
# file for complete list of available options

# You can use https://djecrety.ir to generate a key
SECRET_KEY=

# Application database
POSTGRES_USER=
POSTGRES_PASSWORD=

# Dummy iShelters
ISHELTERS_USERNAME=
ISHELTERS_PASSWORD=

DEBUG=True
ALLOWED_HOSTS=*
DJANGO_PORT=8000
# Note that this will disables Google SSO
# and the app will be in read-only mode, regardless
# of assigned role
# See the docs for more information
REQUIRE_AUTH=False
ETL_EMAIL_REPORT=False
CORS_ALLOW_ALL_ORIGINS=True
VITE_REQUIRE_AUTH=${REQUIRE_AUTH}
VITE_JSON_SERVER_URL=http://localhost:${DJANGO_PORT}
```

### Dev Container

A [dev container](https://containers.dev) is included with this project to
streamline and simplify collaborative development. This is a docker container
with all application dependencies and tools. This is the preferred and
recommended way to develop on this project.

While dev containers are supported by a number of [different tools and services](https://containers.dev/supporting) this particular configuration (described in [.devcontainer.json](.devcontainer/devcontainer.json)) is tailored towards [Visual Studio Code](https://code.visualstudio.com).

1. Open VS Code
2. If not installed, install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
3. Open the project in VS Code.

   Once the project is loaded you should get a
   prompt in the bottom-right corner to **"Reopen in Container"**. Click it to
   reopen the project in the dev container.

4. If you did not receive the **"Reopen in Container"** prompt:

   1. Open VS Code Command Palette
   2. Type in `Dev Containers` and select **"Reopen in Container"**

Barring any issues, this will:

- pull and build all the necessary image
- bring up the development stack (db, django, react, and dummy ishelters)
- initialize the databases
- prompt for the default super user

Once it is complete, check Docker Desktop. All services under `...vms` should be green (running).

In your browser visit [http://localhost](http://localhost) and ta-da!

See [below for information](#accessing-container-applications-and-services) on
accessing other containers from _within_ your dev container.

Happy coding!!

## Accessing container applications and services

Unless otherwise noted, most application/services/tools running in containers
are accessible on their default ports on localhost _outside_ a container.
For example, `localhost:5432` connects you to the database container.

If/when you need to access the host machine from _within_ another container
(like your [devcontainer](#dev-container)) use `host.docker.internal` as the
hostname. This is a [special DNS Docker provides](
   https://www.docker.com/blog/how-docker-desktop-networking-works-under-the-hood/)
for containers to access services running on the host machine.

# Makefile

For convenience a [makefile](<https://en.wikipedia.org/wiki/Make_(software)>) is included with this project
to streamline a number of repetitive tasks. A helpful explanation and tutorial
of Make is available [here](https://makefiletutorial.com).

Executing a make command looks like this:

`make target`

where `target` is any target specified in the makefile.

Assuming you have `make`, you can run any of the targets listed below. Note
that some targets (e.g., `sync, super, migrate`) run in the context of the
Django container and will raise an error when it is not running.

| **Target**     | **Description**                                                                                            |
|----------------|------------------------------------------------------------------------------------------------------------|
| init           | Spin up the development environment. This is the default target if one is not provided (e.g. `make`)       |
| build          | Build application docker images                                                                            |
| up             | Bring up the application docker compose stack (start the app)                                              |
| down           | Bring down the application docker compose stop (stop the app)                                              |
| restart        | Stop then restart the stack                                                                                |
| login          | Log into the specified container e.g. `make login container=django`                                        |
| clean          | Stop the app and remove volumes and other build files. Effectively start<br>from scratch at the next `up`. |
| cleaninit      | Combine `clean + init`. Effectively start<br>from scratch at the next `up`.                                |
| cleanishelters | Destroy and rebuild the iShelters dev database (MySQL)                                                     |
| cleanvms       | Destroy and rebuild the application database (PostgreSQL)                                                  |
| cleandbs       | Combine cleaning the vms & ishelters. Effectively start<br>from scratch at the next `up`.                  |
| makemigrations | creates new migration files based on the changes detected in the models                                    |
| migrate        | Synchronize change made to models with the schema in the database                                          |
| mimesis        | Load fake data generated using mimesis into<br>development iShelters database                              |
| sync           | Synchronize iShelters with VMS (i.e., copy volunteer data from iShelters to VMS)                           |
| super          | Create a new Django admin super user                                                                       |

_Generated using [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables#)_

## Using makefile on Windows

Windows does not support make files natively. However, if you have installed/enabled WSL,
you can open a WSL terminal to use the makefile.
