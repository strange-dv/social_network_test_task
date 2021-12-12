FROM python:3.9.6-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN apk update \
    && apk add libffi-dev postgresql-dev gcc python3-dev musl-dev

WORKDIR /application

RUN pip3 install --upgrade pip
COPY requirements.txt /application/
RUN pip3 install -r requirements.txt

COPY . /application/
