app:=

all:
	echo "Makefile settings"

setup:
	pip install -r requirements.txt

setup-dev: setup
	pip install -r requirements_dev.txt

run:
	python manage.py runserver

check:
	python manage.py check

shell:
	python manage.py shell

dbshell:
	python manage.py dbshell

m-show:
	python manage.py showmigrations

m-create:
	python manage.py makemigrations $(app)

m-migrate:
	python manage.py migrate $(app)

format:
	pycln . --config pyproject.toml
	isort . --settings-path pyproject.toml
	black . --config pyproject.toml
