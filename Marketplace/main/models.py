from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    title_product = models.CharField(max_length=100, help_text='введите название продукта')
    description_product = models.TextField(blank=True, help_text='введите описание товара')
    price_product = models.DecimalField(max_digits=20, decimal_places=5, help_text='укажите цену')
    created_product = models.DateTimeField(auto_now_add=True)
    saleman_product = models.ForeignKey('SaleMan', on_delete=models.CASCADE, null=True, related_name='saleman_product')
    tag_product = models.ManyToManyField('TagProduct', related_name='tag_product')
    category_product = models.ForeignKey('CategoryProduct', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title_product
    def get_absolute_url(self):
        return reverse('good-detail',args = [str(self.id)])


class SaleMan(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    e_mail = models.EmailField(max_length=100,blank=True)
    article = models.CharField(max_length=20, default='default-article')
    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'


    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class CategoryProduct(models.Model):
    title_category = models.CharField(max_length=100,help_text='введите категорию товара')

    class Meta:
        verbose_name = 'Категория'

    def __str__(self):
        return self.title_category

class TagProduct(models.Model):
    title_tag = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тэги'

    def __str__(self):
        return self.title_tag


class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    #new_good = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self):
        return str(self.user)



# Create your models here.
