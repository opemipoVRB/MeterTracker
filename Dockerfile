FROM python:3.7-alpine
MAINTAINER 3megawatt

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /threemegawatt

WORKDIR /threemegawatt

COPY ./threemegawatt /threemegawatt

RUN adduser -D user

USER user
