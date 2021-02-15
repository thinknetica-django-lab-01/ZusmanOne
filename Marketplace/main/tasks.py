from Marketplace.celery import app
from .logic import send_new_good
from .models import Product

@app.task
def send_celery_mail(Product):
    send_new_good(Product)