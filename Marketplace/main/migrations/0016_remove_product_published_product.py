# Generated by Django 3.1.5 on 2021-02-11 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210211_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='published_product',
        ),
    ]
