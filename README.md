# Angel Among Us Volunteer Management System

Volunteer management system using a Django REST backend (via [Django REST framework
](https://www.django-rest-framework.org))
with a React (via [React-Admin](https://marmelab.com/react-admin/)) frontend.

# Getting Started

**Instructions and setup below are for development and should not be used when deploying
to production. See the [deployment instructions](#deployment) below for that**.

## Perquisites

To get the project up and running, you'll need:

- [Docker](https://www.docker.com)

  - If installing on Windows, you may need to install/enable [WSL-2](https://learn.microsoft.com/en-us/windows/wsl/install) first.

- You IDE of choice
- Some familiarity with terminal/command prompt

  - If using Windows, it's recommended to install & use [Windows Terminal](https://learn.microsoft.com/en-us/windows/terminal/install).

- If on Windows, [show/enable hidden files](https://support.microsoft.com/en-us/windows/view-hidden-files-and-folders-in-windows-97fbc472-c603-9d90-91d0-1166d1d9f4b5)

This is a fully containerized stack, as such there's no need to install anything locally. The project is shared (mounted) to the container
and changes are synced both ways.

## Running It

### Environment file

First things first is to create your environment file. This file defines
environment variables that are accessible from any process.

1. In the project folder make a copy of `example.env` and name it `.env` (note the dot in the file name)
2. Edit `.env` by filling in the required settings

<!-- From here, you have a couple of options of development environment: -->

<!-- - [Dev container](#dev-container) - simple & easy -->
<!-- - [Local](#local) - your milage may vary -->

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

See [below for information](#accessing-container-applications-and-services) on
accessing other containers from _within_ your dev container.

<!-- ### Local

To develop locally, you'll need to install Python & add it to your system PATH.

Additionally, instead of installing Python packages system wide it's best to use
a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/#how-can-you-work-with-a-python-virtual-environment).

A [makefile](#makefile) is included with this project to streamline repetitive
tasks. You can use it instead running commands directly.

Assuming Docker is running:

1. Open a terminal/command prompt
2. In the terminal, navigate to the project folder

   ```shell
   # if on Windows the path separator would be \ instead of /
   cd /path/to/angels-among-us-vms
   ```

3. Install project dependencies

   ```shell
   pip install -r requirements.txt
   ```

4. Build the project's docker image:

   ```shell
   docker build -t aau-vms .
   ```

5. Bring up the application stack

   ```shell
   docker compose up -d
   ``` -->

If there are no issues, this will build and pull all the necessary images. Once
it is complete, check Docker Desktop. All services under `vms` should be green (running).

In your browser visit [http://localhost](http://localhost) and ta-da!

Happy coding!!

## Accessing container applications and services

Unless otherwise noted, most application/services/tools running in containers
are accessible on their default ports on localhost _outside_ of the container.
For example, `localhost:5432` connects you to the database container
_if it is running_.

If/when you need to access the host machine from _within_ a container
(say a [devcontainer](#dev-container)) use `host.docker.internal` as the
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

Assuming you have make installed, you can run any of the targets listed below.

|   **Target**   |                                              **Description**                                              |
|:--------------:|:---------------------------------------------------------------------------------------------------------:|
|      init      |    Spin up the development environment. This is the default target if one is not provided (e.g. `make`)   |
|      build     |                                      Build application docker images                                      |
|       up       |                       Bring up the application docker compose stack (start the app)                       |
|      down      |                       Bring down the application docker compose stop (stop the app)                       |
|      login     |                      Log into the specified container e.g. `make -e login container=djagno`               |
|      clean     |              Stop the app and remove volumes. Effectively start from scratch on the next `up`             |
|     cleandb    | Stop the db container & remove its volumes. Effectively start the database from scratch on the next  `up` |
| makemigrations |                  creates new migration files based on the changes detected in the models                  |
|     migrate    |                     Synchronize change made to models with the schema in the database                     |
|   djangotest   |                                         Run all backend unit tests                                        |

_Generated using [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables#)_

## Using makefile on Windows

Windows does not support makefiles natively. However, if you have installed/enabled WSL,
you can open a WSL terminal to use the makefile.

# Deployment

TODO

# Troubleshooting

Common gotchas and resolution

## ModuleNotFoundError

When using the [dev container](#dev-container) you may get this error,
even after running `pip install`. This is because the container builds
and installs packages as `root` but runs as `vscode` user (at time of writing).

To fix this: add the package to [the requirements file](./requirements.txt)
then rebuild the container.
