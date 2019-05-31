FROM python:3.7-alpine
MAINTAINER beanalytic

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /aapp
WORKDIR /aapp
COPY ./aapp /aapp

RUN adduser -D user
USER user
