from apscheduler.schedulers.background import BackgroundScheduler
import datetime, pytz
from .models import *
from django.template.loader import get_template
from django.core.mail import send_mail, EmailMultiAlternatives

#планировщик задач

scheduler = BackgroundScheduler()
job = None

def product_week():
    OurTZ = pytz.timezone('Europe/Moscow')
    last_week = datetime.datetime.now(OurTZ) - datetime.timedelta(days=7)
    product_week = Product.objects.filter(created_product__gte=last_week)
    html_week = get_template('edit/mail_week.html')
    html_data = {'last_week': product_week}
    week_html = html_week.render(html_data)
    message_week = EmailMultiAlternatives(subject='product week',body=week_html,
                                          to=[Subscriber.objects.values("user__email")])
    message_week.content_subtype = 'html'
    message_week.send()


def start_job():
    global job
    job = scheduler.add_job(product_week, 'interval', days=7)
    try:
        print('запуск планировщика')
        scheduler.start()
    except KeyboardInterrupt:
        print('остановка планировщика')
        scheduler.shutdown()
