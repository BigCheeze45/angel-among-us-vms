#!/bin/bash

INITIALIZATION_FILE=".devcontainer/.pdk"

# Avoid dubious ownership in dev container:
# https://www.kenmuse.com/blog/avoiding-dubious-ownership-in-dev-containers/
git config --global --add safe.directory "$CONTAINER_WORKSPACE_FOLDER"

# Build application image & start the stack
if [ ! -f "$INITIALIZATION_FILE" ]; then
    # file doesn't exist; run first time setup
    make init

    # install pre-commit hooks
    pre-commit install

    # setup node modules
    cd react-admin && npm install && cd ..
    echo "This file tracks whether dev container has been initialized. It is safe to delete." >$INITIALIZATION_FILE
else
    # init has been ran before so just bring stuff up
    make up
fi
