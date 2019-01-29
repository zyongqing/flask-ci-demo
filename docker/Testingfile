FROM python:3-alpine

ENV FLASK_APP="manage.py"
ENV FLASK_ENV="development"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
CMD ["flask", "cov"]
