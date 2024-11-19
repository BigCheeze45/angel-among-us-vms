# Accessing container applications and services

Unless otherwise noted, most application/services/tools running in containers
are accessible on their default ports on localhost _outside_ a container.
For example, `localhost:5432` connects you to the database container.

If/when you need to access the host machine from _within_ another container
(like your [devcontainer](./dev.md#containerization)) use `host.docker.internal` as the
hostname. This is a [special DNS Docker provides](
   https://www.docker.com/blog/how-docker-desktop-networking-works-under-the-hood/)
for containers to access services running on the host machine.
