FROM python:3.8.10-alpine

WORKDIR /usr/src/app_car_reviews

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./requirements.txt .
COPY ./Pipfile .
COPY ./Pipfile.lock .

# RUN pipenv shell


COPY . .

RUN pipenv install -r requirements.txt