# Generated by Django 3.1.5 on 2021-02-08 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_auto_20210208_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='profile',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
