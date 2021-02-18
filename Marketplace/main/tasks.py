from Marketplace.celery import app
from .logic import send_new_good
from .models import Product

@app.task
def send_celery_mail(product_id): #какие параметры должна принимать эта функция?
    queryset = Product.objects.get(pk=product_id)
    send_new_good(Product)