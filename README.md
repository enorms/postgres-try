# Postgres try

Access data on a heroku instance.


## Setup



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

If "relation "hello_greeting" does not exist" create 

Create tables to init db
```
python manage.py migrate
heroku run python manage.py migrate
```

## DB commands

After making changes
```sh
python manage.py makemigrations
python manage.py migrate
heroku run python manage.py makemigrations
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

# Trouble shooting

If access db and a relation "<table_name>" does not exist error, because while the database is configured, the tables have not yet been created.
To create the <table_name> table, run the standard Django manage.py migrate command: `heroku run python manage.py migrate`


# CAUTION

Reset database
```
heroku pg:reset DATABASE
```

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
