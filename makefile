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

# Destroy and rebuild the database
cleandb:
	$(DOCKER_COMPOSE) down database --volumes
	$(DOCKER_COMPOSE) up database -d
	sleep 15
	$(MAKE) makemigrations
	$(MAKE) migrate
	$(MAKE) loaddata

# Login into the specified container
login:
	docker exec -ti $(container) /bin/bash

# Synchronize change made to models with the schema in the database
migrate:
	docker exec -t $(DJANGO_CONTAINER) python manage.py migrate

# Dump DB to json file
dumpdata:
	docker exec -t $(DJANGO_CONTAINER) python manage.py dumpdata --output app/fixtures/dumpdata.json

# Load sample fixtures
loaddata:
	docker exec -t $(DJANGO_CONTAINER) python manage.py loaddata app/fixtures/dumpdata.json

# This command creates new migration files based on the changes detected in the models.
makemigrations:
	docker exec -t $(DJANGO_CONTAINER) python manage.py makemigrations app

# Create a new Django admin super user
super:
	docker exec -ti $(DJANGO_CONTAINER) python manage.py createsuperuser

# Run backend (django) tests
djangotest:
	docker exec -t $(DJANGO_CONTAINER) python manage.py test --noinput --failfast app/tests

# Initialize: print welcome message, build image, and bring up the stack
.PHONY: init
init:
	@echo "Setting up VMS Developemnt environment"
	$(MAKE) build
	$(MAKE) up
	# FIXME - Hack until dependencies & health checks can be added
	sleep 15
	$(MAKE) migrate
	$(MAKE) loaddata
	@echo "Happy coding!"
