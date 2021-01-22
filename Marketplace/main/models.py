from django.db import models


class Product(models.Model):
    title_product = models.CharField(max_length=100, help_text='введите название продукта')
    description_product = models.TextField(blank=True, help_text='введите описание товара')
    price_product = models.DecimalField(max_digit=10, decimal_places=10, help_text='укажите цену')
    created_product = models.DateTimeField(auto_now_add=True)
    saleman_product = models.ForeignKey('SaleMan', null=True, on_delte=models.SET_NULL)


class SaleMan(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    e_mail = models.EmailField(max_length=100)

class CategoryProduct(models.Model):
    title_category = models.CharField(max_length=100,help_text='введите категорию товара')

class TagProduct(models.Model):
    title_tag = models.CharField(max_length=100)

# Create your models here.
