.PHONY: run test cov

FLASK_APP_NAME='manage.py'

all: run

run:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='production' flask run --host=0.0.0.0

test:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='development' flask test

cov:
	FLASK_APP=$(FLASK_APP_NAME) FLASK_ENV='development' flask cov