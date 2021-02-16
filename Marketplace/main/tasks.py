from Marketplace.celery import app
from .logic import send_new_good, product_week
from .models import Product

@app.task
def send_celery_mail(Product):
    send_new_good(Product)


@app.task
def send_week_mail():
    product_week()