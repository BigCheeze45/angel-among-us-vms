FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

ADD requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
    # dev tools, not needed for prod
    pre-commit \
    python-dotenv \
    # install project dependcies
    --requirement /tmp/requirements.txt

# Clean up
RUN rm -f /tmp/requirements.txt
