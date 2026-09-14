FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install libpq5 -y

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --workers 4 --bind 0.0.0.0:8000 main.wsgi

