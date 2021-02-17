from Marketplace.celery import app
from .logic import send_new_good
from .models import Product

@app.task
def send_celery_mail():
    send_new_good()

#
# @app.task
# def send_week_mail():
#     product_week()