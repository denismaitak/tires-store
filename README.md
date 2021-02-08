# tires-store
Example of Django project

## Run project

```bash
$ cd tires-store
```

```bash
$ python3.8 -m venv .virtualenv
```

```bash
$ source .virtualenv/bin/activate
```

```bash
$ pip install -r requirements/development.txt
```

```bash
$ docker-compose up -d postgres
```

```bash
$ ./manage.py migrate
```

```bash
$ ./manage.py createsuperuser
```

```bash
$ ./manage.py runserver
```

## Set up GIT-hooks if you need it.

```bash
$ inv copygithooks
```

Get fun!
