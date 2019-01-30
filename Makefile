.PHONY: app app-dev job job-dev test cov shell pip-lock

FLASK_APP_NAME='manage.py'

all: app

app:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='production' flask run --host=0.0.0.0

app-dev:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='development' flask run --host=0.0.0.0

job:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='production' celery -A manage.celery worker

job-dev:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='production' celery -A manage.celery worker -c 1 --loglevel=debug

test:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='development' flask test

cov:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='development' flask cov

shell:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='development' flask shell

pip-lock:
	pipenv lock --requirements > requirements.txt
	pipenv lock --requirements --dev > requirements-dev.txt