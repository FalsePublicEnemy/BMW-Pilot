FROM python:3.9.6

LABEL Author="KyivNerds"

# ENV PYTHONBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD python3 manage.py makemigrations && python3 manage.py migrate
# RUN python3 manage.py migrate
