FROM python AS backend

# Update package repository list
RUN apt-get update -y
# Add requirements file. This will be used to install
COPY requirements.txt /tmp
# Update pip & any requirements
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --requirement /tmp/requirements.txt

# Clean up
RUN rm /tmp/requirements.txt

# Build frontend image
# https://www.docker.com/blog/how-to-setup-your-local-node-js-development-environment-using-docker/
FROM node AS frontend

WORKDIR /app
COPY react-admin/package*.json .
RUN npm install

COPY react-admin .

CMD ["npm", "run", "dev"]
