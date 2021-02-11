from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django_apscheduler.models import DjangoJobExecution
from django.utils import timezone
from .views import *
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import *
from django.shortcuts import render
import datetime, pytz



def last_week():
    week_html = get_template('edit/newgood.html')
    data_week={'product':Product}
    body_week = week_html.render(data_week)
    msg_week = EmailMultiAlternatives(subject='плановая рассылка',body=body_week,
                                      to=[Subscriber.objects.values('user__mail')])
    msg_week.attach_alternative(body_week,'text/html')
    OurTZ = pytz.timezone('Europe/Moscow')
    last_week = datetime.datetime.now(OurTZ) - datetime.timedelta(days=2)
    if Product.objects.filter(created_product__gte=last_week):
        msg_week.send()


def start():
    scheduler = BackgroundScheduler
    scheduler.add_jobstore(DjangoJobStore(),'default')
    scheduler.add_job(
        last_week(),
        'interval', minute = 1,
        id = 'my_job',
        jobstore = 'default',
    )
        register_events(scheduler)
        replace_existing = True,
        scheduler.start()
