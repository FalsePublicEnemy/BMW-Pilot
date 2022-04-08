FROM python:3.9.6

LABEL Author="KyivNerds"

ENV PYTHONBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

RUN pip install -r requirements.txt
