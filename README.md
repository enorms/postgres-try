# Postgres try

Access data on a heroku instance.


## Setup

if push heroku main failes
disable collect static files
```
heroku config:set DISABLE_COLLECTSTATIC=1
```

## Endpoints


/db

## Commands

Push to heroku
```sh
git push heroku main
```

Open remote in browser
```sh
heroku open
```

Check logs
```sh
heroku logs --tail
```

Create tables to init db
```
heroku run python manage.py migrate
```

## DB commands

After making changes
```sh
python manage.py makemigrations
python manage.py migrate
# push changes

heroku run manage.py makemigrations
heroku run python manage.py migrate
```

## Account commands

Show environment variables
```
heroku config
```

Show databases
```
heroku addons
```

Show postgres details
```
heroku pg
```

Chech hours remaining
```
heroku ps
```

Shacle dyno up to 1
```sh
heroku ps:scale web=1
```

# CAUTION

Reset database
```
heroku pg:reset DATABASE_URL --confirm <database_name>
```

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
