FROM python:3.9.8-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /app
COPY . /app/
RUN mkdir -p /app/static
RUN pip install --upgrade pip
RUN pip install -r requirements.txt