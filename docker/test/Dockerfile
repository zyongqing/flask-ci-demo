FROM python:3.7-alpine

ENV FLASK_APP="manage.py"
ENV FLASK_ENV="development"

COPY . /app

WORKDIR /app

RUN mkdir -p instance && \
    cp docker/test/conf/flask/config_small.py instance/config.py

RUN apk add --update build-base && \
    pip install -i https://pypi.douban.com/simple/ --upgrade pipenv && \
    pipenv install --dev

CMD ["pipenv", "run", "flask", "cov", "small"]
