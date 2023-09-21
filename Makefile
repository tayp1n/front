PROJECT_DIR=$(shell pwd)

SERVICE_NAME = dash-app

SYSTEM_PYTHON=python3
SYSTEM_PYTHON_38=python3.8
SYSTEM_PYTHON_39=python3.9

SERVICES_DIR=$(PROJECT_DIR)

SERVICE_SERVICE_DIR=$(SERVICES_DIR)
SERVICE_ENV_DIR?=$(SERVICE_SERVICE_DIR)/venv
SERVICE_PYTHON?=$(SERVICE_ENV_DIR)/bin/python3

SERVICE_APP_DIR=$(SERVICE_SERVICE_DIR)/app

.PHONY: service_flake8 service_mypy service_black service_run service_run_console

service_check_code: service_black service_flake8 service_mypy

service_black:
	cd $(SERVICE_SERVICE_DIR) && \
	poetry run black $(SERVICE_APP_DIR)

service_flake8:
	cd $(SERVICE_SERVICE_DIR) && \
	poetry run flake8 $(SERVICE_APP_DIR)

service_mypy:
	cd $(SERVICE_SERVICE_DIR) && \
	poetry run mypy $(SERVICE_APP_DIR)

service_test:
	cd $(SERVICE_SERVICE_DIR) && \
	ls -la && \
	poetry run pytest -vv

service_run:
	ls -la && \
	source $(SERVICE_ENV_DIR)/bin/activate && \
	SETTINGS_MODULE=local $(SERVICE_PYTHON) $(SERVICE_SERVICE_DIR)/__main__.py