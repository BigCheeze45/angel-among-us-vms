FROM python

# Update package repository list
RUN apt-get update -y
# Add requirements file. This will be used to install
ADD requirements.txt /tmp
# Update pip & any requirements
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --requirement /tmp/requirements.txt

# Clean up
RUN rm /tmp/requirements.txt
