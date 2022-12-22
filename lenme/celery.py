from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
# "sample_app" is name of the root app
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lenme.settings')

app = Celery( 'lenme')
app.config_from_object("django.conf:settings", namespace="CELERY")
            
# Load task modules from all registered Django apps. 
app.conf.enable_utc = False  # because we are using time of Africa/Cairo
app.conf.update(timezone="Africa/Cairo")
app.conf.update(enable_utc=False)
app.conf.update(broker_url=settings.CELERY_BROKER_URL)
app.autodiscover_tasks()

