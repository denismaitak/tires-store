# tires-store
Example of Django project

## Run the project

### Create virtual environment

```bash
$ cd tires-store
```

```bash
$ python3.8 -m venv .virtualenv
```

```bash
$ source .virtualenv/bin/activate
```

### Install requirements

```bash
$ pip install -r requirements/development.txt
```

### Run Docker-containers

```bash
$ docker-compose up -d postgres
```

### Set up local settings file

```bash
$ cp config/settings/local.py.template config/settings/local.py
```

### Run Django

```bash
$ ./manage.py migrate
```

```bash
$ ./manage.py createsuperuser
```

```bash
$ ./manage.py runserver
```

## Set up GIT-hooks if you need it

```bash
$ inv copygithooks
```

## Run Celery

Full workflow requires worker and broker

```bash
$ celery --app config.celery:app worker -l info
```

```bash
$ celery --app config.celery:app beat -l info -S django
```

Get fun!
