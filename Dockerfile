ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*
RUN pip install pipenv
RUN pipenv install

RUN pipenv run manage.py collectstatic --noinput

EXPOSE 8000

WORKDIR /wookieepedia
CMD ["pipenv", "run", "daphne", "wookieepedia.asgi:application"]