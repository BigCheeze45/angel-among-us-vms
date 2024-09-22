# Variables
DOCKER_COMPOSE=docker compose
DJANGO_CONTAINER=django

# Default target
.PHONY: all
all: init

# Build the Docker images
build:
	@echo "Building Django image"
	docker build --target backend -t aau-vms-backend .
	@echo "Building React-Admin image"
	docker build --target frontend -t aau-vms-frontend .

# Bring up the Docker Compose stack
up:
	$(DOCKER_COMPOSE) up -d

# Bring down the Docker Compose stack
down:
	$(DOCKER_COMPOSE) down

# Reset: bring down the stack, remove volumes and orphaned containers
clean:
	$(DOCKER_COMPOSE) down --volumes --remove-orphans
	rm -f .devcontainer/.pdk
	rm -fr react-admin/node_modules

# Login into the specified container
login:
	docker exec -ti $(container) /bin/bash

# Synchronize change made to models with the schema in the database
migrate:
	docker exec -t $(DJANGO_CONTAINER) python manage.py migrate

# This command creates new migration files based on the changes detected in the models.
makemigrations:
	docker exec -t $(DJANGO_CONTAINER) python manage.py makemigrations app

# Create a new Django admin super user
super:
	docker exec -ti $(DJANGO_CONTAINER) python manage.py createsuperuser

# Initialize: print welcome message, build image, and bring up the stack
.PHONY: init
init:
	@echo "Setting up VMS Developemnt environment"
	$(MAKE) build
	$(MAKE) up
	# Hack until dependencies & health checks can be added
	sleep 15
	$(MAKE) migrate
	$(MAKE) super
	@echo "Happy coding!"
