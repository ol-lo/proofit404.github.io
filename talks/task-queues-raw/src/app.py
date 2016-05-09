import os

from celery import Celery

app = Celery(__name__)


@app.task
def add(x, y):
    return x + y


if os.getenv('redis_broker'):
    app.conf.broker_url = 'redis://localhost:6379/0'
    app.conf.result_backend = 'redis://localhost:6379/1'
else:
    app.conf.broker_url = 'amqp://guest:guest@localhost:5672/pyconru/'
    app.conf.result_backend = 'redis://localhost:6379/2'
