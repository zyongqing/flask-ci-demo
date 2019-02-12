FROM python:3.6-alpine

ENV FLASK_APP="manage.py"
ENV FLASK_ENV="production"

COPY . /app

WORKDIR /app

RUN mkdir -p instance && \
    cp docker/app/conf/flask/config.py instance

RUN pip install -i https://pypi.douban.com/simple/ --upgrade pipenv && \
    pipenv install

CMD ["pipenv", "run", "flask", "run", "--host", "0.0.0.0"]