import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SchoolHairAndMakeUP.settings')

app = Celery('shop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app_course = Celery('courses')
app_course.config_from_object('django.conf:settings')
app_course.autodiscover_tasks(lambda: settings.INSTALLED_APPS)