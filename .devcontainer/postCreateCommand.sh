#!/bin/bash

INITIALIZATION_FILE=".devcontainer/.pdk"

# Avoid dubious ownership in dev container:
# https://www.kenmuse.com/blog/avoiding-dubious-ownership-in-dev-containers/
git config --global --add safe.directory "$CONTAINER_WORKSPACE_FOLDER"

# #CMD ["npm", "run", "dev"]
# https://stackoverflow.com/a/61137716
# CMD [ -d "node_modules" ] && npm run dev || npm ci && npm run dev
if [ ! -d "react-admin/node_modules" ]; then
    # setup local node modules
    cd react-admin && npm ci && cd ..
fi

# Build application image & start the stack
if [ ! -f "$INITIALIZATION_FILE" ]; then
    # file doesn't exist; run first time setup
    make init
    echo "This file tracks whether dev container has been initialized. It is safe to delete." >$INITIALIZATION_FILE
else
    # init has been ran before so just bring stuff up
    make up
fi
