# Generated by Django 3.1.5 on 2021-01-25 13:26

from django.db import migrations,models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210125_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleman',
            name='article',
            field=models.CharField(max_length=10)
        )
    ]
