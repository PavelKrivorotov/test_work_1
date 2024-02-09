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

# May be need add two bash files:
# 1) migrations.sh: run migrations -> (python manage.py run migrations)
# 2) celery.sh:     run celery -> (celery -A main worker)

# 
ENTRYPOINT python main/manage.py runserver ${host}:${port}
