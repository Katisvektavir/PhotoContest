FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --workers 4 --bind 0.0.0.0:8000 best_site.wsgi

