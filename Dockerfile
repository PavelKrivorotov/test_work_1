# syntax=docker/dockerfile:1

# Set base image and workdir
FROM python:3.10-alpine3.15
WORKDIR /app

# Copy requirements and install
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy env variables
COPY ./.docker.env /app/.env

# Copy source code
COPY ./main /app/main

# ...
ENV host=0.0.0.0
ENV port=8000

# Copy running bash scripts;
COPY ./run-django-app.sh /app/run-django-app.sh
COPY ./run-celery.sh /app/run-celery.sh

RUN chmod +x /app/run-django-app.sh
RUN chmod +x /app/run-celery.sh
