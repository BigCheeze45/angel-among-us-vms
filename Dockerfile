FROM python

# Update package repository list
RUN apt-get update -y
# Add requirements file. This will be used to install
ADD requirements.txt /tmp
# Update pip & any requirements
RUN pip install -U pip \
    && pip install -r /tmp/requirements.txt

# Clean up
RUN rm /tmp/requirements.txt
