# Generated by Django 3.1.5 on 2021-01-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210124_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_product',
            field=models.DecimalField(decimal_places=5, help_text='укажите цену', max_digits=20),
        ),
    ]
