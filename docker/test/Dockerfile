FROM python:3.6-alpine

ENV FLASK_APP="manage.py"
ENV FLASK_ENV="development"

COPY . /app
WORKDIR /app

RUN mkdir -p instance && \
    cp docker/app/conf/flask/config.py instance

RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
CMD ["flask", "cov"]
