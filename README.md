[![Travis](https://travis-ci.org/zyongqing/flask-ci-demo.svg?branch=master)](https://travis-ci.org/zyongqing/flask-ci-demo)
[![](https://img.shields.io/github/license/zyongqing/flask-ci-demo.svg?style=flat)]()

# FLASK-CI-DEMO

This is a demo project only for CI/CD training and practice.

## Local Run

```bash
make app           # run flask app
make job           # run celery worker
make app-dev       # run flask app in debug mode
make job-dev       # run celery worker in debug mode
make test          # run all unittest
make cov           # run code coverage
make shell         # run flask shell
```

## Docker Local Build

```bash
docker-compose build       # build all service
docker-compose build app   # build only flask app service
docekr-compose build job   # build only celery service
docker-compose build test  # build only test service
```

## Docker Local Run

```bash
docker-compose run -p 80:80 web       # run entire flask services
docker-compose run -p 5000:5000 app   # run only flask app service
docker-compose run job                # run only celery service
docker-compose run test               # run only test service
```

## Docker Release Run

```bash
docker-compose -f docker-compose_release.yml up   # start entire services
docker-compose -f docker-compose_release.yml down # stop & clean entire services
```


## Docker Repository
[![](https://img.shields.io/badge/zyongqing%2Fflask--ci--demo--web-latest-green.svg?style=flat)](https://cloud.docker.com/repository/docker/zyongqing/flask-ci-demo-web)

[![](https://img.shields.io/badge/zyongqing%2Fflask--ci--demo--app-latest-green.svg?style=flat)](https://cloud.docker.com/repository/docker/zyongqing/flask-ci-demo-web)
