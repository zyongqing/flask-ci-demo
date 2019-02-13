.PHONY: app job test cov shell

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

test: test-small

test-all: test-small test-medium test-large

test-small:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='development' flask test small

test-medium:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='development' flask test medium

test-large:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='development' flask test large

cov: cov-small

cov-all: cov-small cov-medium cov-large

cov-small:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='development' flask cov small

cov-medium:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='development' flask cov medium

cov-large:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='development' flask cov large

shell:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='development' flask shell
