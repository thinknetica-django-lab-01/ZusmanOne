from Marketplace.celery import app
from .logic import send_new_good
from .models import Product

@app.task
def send_celery_mail(Product): #какие параметры должна принимать эта функция?
    send_new_good(Product)