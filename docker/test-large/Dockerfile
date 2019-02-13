FROM python:3.6-alpine

ENV FLASK_APP="manage.py"
ENV FLASK_ENV="development"

COPY . /app

WORKDIR /app

RUN mkdir -p instance && \
    cp docker/test-large/conf/flask/config.py instance

RUN pip install -i https://pypi.douban.com/simple/ --upgrade pipenv && \
    pipenv install --dev

CMD ["pipenv", "run", "flask", "cov", "large"]
