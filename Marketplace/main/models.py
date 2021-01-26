from django.db import models


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


class SaleMan(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    e_mail = models.EmailField(max_length=100,blank=True)

    class Meta:
        verbose_name = 'Продавец'


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
        verbose_name = 'Тэги '

    def __str__(self):
        return self.title_tag

# Create your models here.
