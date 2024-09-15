FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

ADD requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    # install project dependcies
    && pip install --no-cache-dir --requirement /tmp/requirements.txt

# Clean up
RUN rm -f /tmp/requirements.txt
