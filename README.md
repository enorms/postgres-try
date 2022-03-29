# Postgres try

Access data on a heroku instance.


## Setup

if push heroku main failes
disable collect static files
```
heroku config:set DISABLE_COLLECTSTATIC=1
```

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

## Account commands

Chech hours remaining
```
heroku ps
```

Shacle dyno up to 1
```sh
heroku ps:scale web=1
```

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
