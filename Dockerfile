# Pull base image
FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /ezop_project

EXPOSE 5432

# Install dependencies
RUN pip install pipenv
COPY ./Pipfile /ezop_project/Pipfile
RUN pipenv install --system --skip-lock

# Copy project
COPY . /ezop_project/
