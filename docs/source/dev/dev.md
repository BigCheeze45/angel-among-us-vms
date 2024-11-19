(development)=
# Containerization
This section of the docs describe setting a development environment. The entire
stack (both application and development) is containerized out of the box. As such,
there is no need to install anything locally!

A [dev container](https://containers.dev) configuration is included to
streamline and simplify collaborative development. This is a
docker container with all application dependencies and tools. This is
the recommended way to develop on this project.

While dev containers are supported by a number of [different tools and services](
https://containers.dev/supporting) this project's configuration (described
in `.devcontainer/devcontainer.json`) is tailored towards
[Visual Studio Code](https://code.visualstudio.com).

The rest of this documentation assumes you are using VS Code.

(prereqs)=
# Perquisites
To get the project up and running, you'll need:

- [Docker](https://www.docker.com)
  - If installing on Windows, you may need to install/enable [WSL-2](https://learn.microsoft.com/en-us/windows/wsl/install) first.
- VS Code with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed
   - You are welcome to your choice of IDE but your mileage may vary
- Some familiarity with terminal/command prompt
  - If using Windows, it's recommended to install & use [Windows Terminal](https://learn.microsoft.com/en-us/windows/terminal/install).

With the perquisites installed, head over to [quick start](./quickstart.md) to spin up
development environment and see the app in action.
