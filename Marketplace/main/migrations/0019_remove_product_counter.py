# Generated by Django 3.1.5 on 2021-02-19 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210219_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='counter',
        ),
    ]
