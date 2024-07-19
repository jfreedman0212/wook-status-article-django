FROM docker.io/python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv
RUN pipenv install

EXPOSE 8000

WORKDIR /wookieepedia
CMD ["pipenv", "run", "daphne", "wookieepedia.asgi:application"]