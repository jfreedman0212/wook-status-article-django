# Wookieepedia Status Article Data

This app manages data for Status Article nominations for the Wookieepedia (Star Wars wiki). Admins of the app
can import and tweak data for nominations, nominators, and WookieeProjects. The app will then automatically calculate
rankings for a variety of awards based on that data.

See the Project associated with this repository for more information on what's been built versus what is still in-progress.

## Local Setup

To get started, you'll need to install:

- Python 3
- Pip
- Pipenv
  - Look for pipenv in your package manager or run `brew install pipenv` on Mac.
- SQLite (optional, only necessary for development builds; also it's most likely installed already)
- Docker (optional, only necessary for running Postgres locally)
- Postgres Client Libraries
  - Look for `libpq-dev` as a package in your package manager on Linux, or run `brew install postgres` on Mac.

Once you have all of those installed, create a copy of the `.env.example` file and name it `.env`. If you just want
to test it out, that should be all you need to do. However, you will need to change `DATABASE_URL` to a Postgres
connection string if you want to use that instead of SQLite.

Then, run the following from the root of the project:

```shell
pipenv install
pipenv shell
```

This will bring you into a shell with all dependencies installed. Then from here, let's set up the database and create
an admin user:

```shell
python manage.py migrate
python manage.py createsuperuser
```

With the superuser, you can log into Django Admin as an... admin to manage data within the app. With all that done, 
you're ready to run it:

```shell
python manage.py runserver
```

## Deployment

TODO: this will be to Fly.io but isn't quite ready yet. Working on this now.


## Data Model

TODO: make an ERD with mermaid