# Variables
DOCKER_COMPOSE=docker compose
DJANGO_CONTAINER=django

# Default target
.PHONY: all
all: init

# Build the Docker images
build:
	@echo "Building Django image"
	docker build --pull --no-cache --target backend -t aau-vms-backend .
	@echo "Building React-Admin image"
	docker build --pull --no-cache --target frontend -t aau-vms-frontend .

# Bring up the Docker Compose stack
up:
	$(DOCKER_COMPOSE) up -d

# Bring down the Docker Compose stack
down:
	$(DOCKER_COMPOSE) down

restart:
	$(MAKE) down
	$(MAKE) up
# Reset: bring down the stack, remove volumes and orphaned containers
clean:
	$(DOCKER_COMPOSE) down --volumes --remove-orphans
	rm -fr react-admin/dist
	rm -fr react-admin/.env
	rm -fr react-admin/.vite
	rm -f .devcontainer/.pdk
	rm -fr react-admin/node_modules

# Destroy and rebuild the iShelters dev database
cleanishelters:
	$(DOCKER_COMPOSE) down ishelters --volumes
	$(DOCKER_COMPOSE) up ishelters -d
	sleep 15
	$(MAKE) mimesis

# Destroy and rebuild the application database
cleanvms:
	$(DOCKER_COMPOSE) down database --volumes
	$(DOCKER_COMPOSE) up database -d
	$(MAKE) makemigrations
	$(MAKE) migrate
	$(MAKE) super

# Combine cleaning the vms & ishelters
cleandbs:
	$(MAKE) cleanishelters
	$(MAKE) cleanvms

# Login into the specified container
login:
	docker exec -ti $(container) /bin/bash

# Synchronize change made to models with the schema in the database
migrate:
	docker exec -t $(DJANGO_CONTAINER) python manage.py migrate

# This command creates new migration files based on the changes detected in the models.
makemigrations:
	docker exec -ti $(DJANGO_CONTAINER) python manage.py makemigrations app

# Load fake data generated using mimesis into development
# iShelters database
mimesis:
	docker exec -ti $(DJANGO_CONTAINER) python manage.py mimesis

# Synchronize VMS with iShelters
sync:
	docker exec -ti $(DJANGO_CONTAINER) python manage.py sync

# Create a new Django admin super user
super:
	docker exec -ti $(DJANGO_CONTAINER) python manage.py createsuperuser

cleaninit:
	$(MAKE) clean
	$(MAKE) init

# Initialize: print welcome message, build image, and bring up the stack
.PHONY: init
init:
	@echo "Setting up VMS development environment"
	# $(MAKE) build
	$(MAKE) up
	sleep 15
	$(MAKE) migrate
	$(MAKE) mimesis
	$(MAKE) sync
	$(MAKE) super
	@echo "Happy coding!"
