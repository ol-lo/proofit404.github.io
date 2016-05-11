import os

from celery import Celery

if os.getenv('USE_RABBITMQ'):
    kwargs = {
        'broker': 'amqp://pyconru:pyconru@localhost:5672/pyconru',
        'backend': 'redis://localhost:6379/0'
    }

if os.getenv('USE_REDIS'):
    kwargs = {
        'broker': 'redis://localhost:6380/0',
        'backend': 'redis://localhost:6381/0',
    }

app = Celery(__name__, **kwargs)

del kwargs


@app.task
def add(x, y):
    return x + y
