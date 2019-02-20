[![Travis](https://travis-ci.org/zyongqing/flask-ci-demo.svg?branch=master)](https://travis-ci.org/zyongqing/flask-ci-demo)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License](https://img.shields.io/badge/License-BSD%202--Clause-deepgreen.svg?style=flat)](https://opensource.org/licenses/BSD-2-Clause)

# FLASK-CI-DEMO

This is a demo project only for CI/CD training and practice.

## Local Run

```bash
make app           # run flask app
make job           # run celery worker
make app-dev       # run flask app in debug mode
make job-dev       # run celery worker in debug mode
make test          # run small test
make test-all      # run all test
make test-small    # run small test
make test-medium   # run medium test
make test-large    # run large test
make cov           # run small code coverage
make cov-all       # run all code coverage
make cov-small     # run small test code coverage
make cov-medium    # run medium code coverage
make cov-large     # run large code coverage
make shell         # run flask shell
```

## Docker Local Build

```bash
docker-compose build              # build all service
docker-compose build app          # build only flask app service
docekr-compose build job          # build only celery service
docker-compose build test-small   # build only small test service
docker-compose build test-medium  # build only medium test service
docker-compose build test-large   # build only large test service
```

## Docker Local Run

```bash
docker-compose run -p 80:80 web       # run entire flask services
docker-compose run -p 5000:5000 app   # run only flask app service
docker-compose run job                # run only celery service
docker-compose run test-small         # run only small service
docker-compose run test-medium        # run only medium service
docker-compose run test-large         # run only large service
```

## Docker Release Run

```bash
docker-compose -f docker-compose_release.yml up   # start entire services
docker-compose -f docker-compose_release.yml down # stop & clean entire services
```


## Docker Repository
[![](https://img.shields.io/badge/zyongqing%2Fflask--ci--demo--web-latest-green.svg?style=flat)](https://cloud.docker.com/repository/docker/zyongqing/flask-ci-demo-web)

[![](https://img.shields.io/badge/zyongqing%2Fflask--ci--demo--app-latest-green.svg?style=flat)](https://cloud.docker.com/repository/docker/zyongqing/flask-ci-demo-web)
