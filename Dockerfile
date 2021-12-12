FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /application

COPY requirements.txt /application/

RUN pip3 install -r requirements.txt

COPY . /application/
