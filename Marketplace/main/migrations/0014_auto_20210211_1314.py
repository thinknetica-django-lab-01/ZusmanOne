# Generated by Django 3.1.5 on 2021-02-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_product_published_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published_product',
            field=models.DateTimeField(null=True, verbose_name='дата добавления товара'),
        ),
    ]
