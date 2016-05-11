import os

from celery import Celery

app = Celery(__name__)

if os.getenv('USE_RABBITMQ'):
    app.conf.update(
        BROKER_URL='amqp://pyconru:pyconru@localhost:5672/pyconru',
        CELERY_RESULT_BACKEND='redis://localhost:6379/0')
elif os.getenv('USE_REDIS'):
    app.conf.update(
        BROKER_URL='redis://localhost:6380/0',
        CELERY_RESULT_BACKEND='redis://localhost:6381/0')
else:
    raise Exception('Bad')

app.conf.update(
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json')


@app.task
def add(x, y):
    return x + y
