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
clean:
	$(DOCKER_COMPOSE) down --volumes --remove-orphans

# Migrate: The migrate command looks at the INSTALLED_APPS setting
# and creates any necessary database tables according to the database
# settings in vms/settings.py
migrate:
	docker exec -t $(DJANGO_CONTAINER) python manage.py migrate

# By running makemigrations, you’re telling Django that you’ve made some changes
# to your models (in this case, you’ve made new ones) and that you’d like
# the changes to be stored as a migration.
migrations:
	docker exec -t $(DJANGO_CONTAINER) python manage.py makemigrations app

super:
	docker exec -ti $(DJANGO_CONTAINER) python manage.py createsuperuser

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
