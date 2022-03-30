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



# Scratch

add an entry
```sh
(venv) e@en-mbp-14 postgres-try % heroku run python manage.py shell
 ›   Warning: heroku update available from 7.59.4 to 7.60.0.
Running python manage.py shell on ⬢ immense-bayou-67118... up, run.9884 (Free)
Python 3.10.4 (main, Mar 24 2022, 11:40:21) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from simple.models import MySimpleModel
>>> first_entry = MySimpleModel(col="col_name")
>>> first_entry.save()
>>> res = MySimpleModel.get(pk=1)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'MySimpleModel' has no attribute 'get'
>>> res = MySimpleModel.objects.get(pk=1)
>>> res
<MySimpleModel: MySimpleModel object (1)>
>>> res.col
'col_name'
```

may need to stop old shell
```sh
heroku ps
# get PID
heroku ps:stop run.<number>
```