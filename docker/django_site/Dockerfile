FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install libpq5 -y --no-install-recommends

RUN apt-get install gcc -y --no-install-recommends

ENV PIP_EXTRA_INDEX_URL=https://www.piwheels.org/simple

RUN apt-get install libc6-dev -y --no-install-recommends

RUN apt-get install zlib1g-dev -y --no-install-recommends

RUN apt-get install libjpeg-dev -y --no-install-recommends

RUN pip install -r requirements.txt

RUN apt-get install netcat-openbsd

COPY . .

RUN  chmod +x /app/docker/django_site/entrypoint.sh

ENTRYPOINT ["/app/docker/django_site/entrypoint.sh"]

CMD gunicorn --workers 4 --bind 0.0.0.0:8000 main.wsgi

