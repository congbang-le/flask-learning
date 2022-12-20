# flask-learning

Stores sample code to do basic tasks with Python Flask, for example:

- Start a Flask app with healthcheck endpoint `/health` which will response "Health" and 200 OK.
- Using Celery as worker to run asynchronous task called `sum_int`, which will sum 2 integer from request and store the result to postgres database, used redis as broker.
- Using Alembic to run database migrations.