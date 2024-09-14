#!/bin/bash

# Avoid dubious ownership in dev container:
# https://www.kenmuse.com/blog/avoiding-dubious-ownership-in-dev-containers/
git config --global --add safe.directory "$CONTAINER_WORKSPACE_FOLDER"

# install pre-commit hooks
pre-commit install

# Build application image & start the stack
make init
