FROM python:3.10-slim

EXPOSE 5000/tcp

WORKDIR /app

COPY . .

RUN pip install poetry
RUN poetry install