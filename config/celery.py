import os
import socket

from django.conf import settings

from celery import Celery
from kombu import Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

app = Celery(
    main='tires-store',
    backend=settings.CELERY_BACKEND,
    broker=settings.CELERY_BROKER
)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.task_queues = (
    Queue(settings.CELERY_TASK_DEFAULT_QUEUE),
    Queue(socket.gethostname(), expires=86400),
)

app.conf.timezone = 'UTC'
