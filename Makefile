VENV = venv
REQUIREMENTS = requirements/local.txt
PROJECT = bevendo
GLOBAL_PYTHON = /usr/bin/python3
PIP = $(VENV)/bin/pip3
PYTHON = $(VENV)/bin/python3

.PHONY = help setup

help:
	@echo "--------------------------HELP--------------------------"
	@echo "To setup initial environment type:    make setup"
	@echo "To serve the project type:            make serve"
	@echo "To update the environment type:       make update"
	@echo "To delete the entire project type:    make clean_all"
	@echo "--------------------------------------------------------"

update:
	$(PIP) install --upgrade pip
	$(PIP) install -r $(REQUIREMENTS)

serve:
	$(PYTHON) $(PROJECT)/manage.py runserver 0.0.0.0:9000 --settings bevendo.settings.local

make_migrations:
	$(PYTHON) $(PROJECT)/manage.py makemigrations --settings bevendo.settings.local

migrate:
	$(PYTHON) $(PROJECT)/manage.py migrate --settings bevendo.settings.local

clean_project:
	rm -rf $(PROJECT)

clean_apps:
	rm -rf api
	rm -rf client
	rm -rf ext_data

clean_all: clean_project clean_apps
	rm -rf $(VENV)

test:
	$(PYTHON) $(PROJECT)/manage.py test
