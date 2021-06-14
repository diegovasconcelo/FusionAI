FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN python -m pip install -r requirements.txt

COPY . /app/