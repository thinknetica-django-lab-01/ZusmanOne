# Generated by Django 3.1.5 on 2021-02-19 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_product_published_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
