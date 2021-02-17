import os
from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Marketplace.settings')

app = Celery('Marketplace')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# app.conf.beat_schedule = {
#     'send_mail_week':{
#         'task': 'main.tasks.send_week_mail',
#         'schedule': crontab(minute=0,hour='10', day_of_week='monday')
#     }
# }