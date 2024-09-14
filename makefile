# Variables
DOCKER_IMAGE_NAME := aau-vms
DOCKER_COMPOSE=docker compose
DJANGO_CONTAINER := vms-django-1

# Build the Docker image
build:
	docker build -t $(DOCKER_IMAGE_NAME) .

# Bring up the Docker Compose stack
up:
	$(DOCKER_COMPOSE) up -d

# Bring down the Docker Compose stack
down:
	$(DOCKER_COMPOSE) down

# Reset: bring down the stack, remove volumes and orphaned containers
reset:
	$(DOCKER_COMPOSE) down --volumes --remove-orphans

# Migrate: Synchronize change made to models with the schema in the database
migrate:
	docker exec $(DJANGO_CONTAINER) python manage.py makemigrations app
	docker exec $(DJANGO_CONTAINER) python manage.py migrate

# setup a local dev env - OS independent
local:
	pip install --user --requirement requirements.txt

# Initialize: print welcome message, build image, and bring up the stack
.PHONY: init
init:
	@echo "Setting up VMS Developemnt environment"
	$(MAKE) build
	$(MAKE) up
	@echo "Happy coding!"

# Default target
.PHONY: all
all: init
