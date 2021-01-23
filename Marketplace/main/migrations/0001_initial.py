# Generated by Django 3.1.5 on 2021-01-23 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_category', models.CharField(help_text='введите категорию товара', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SaleMan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('e_mail', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TagProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_product', models.CharField(help_text='введите название продукта', max_length=100)),
                ('description_product', models.TextField(blank=True, help_text='введите описание товара')),
                ('price_product', models.DecimalField(decimal_places=10, help_text='укажите цену', max_digits=10)),
                ('created_product', models.DateTimeField(auto_now_add=True)),
                ('category_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.categoryproduct')),
                ('saleman_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='saleman_product', to='main.saleman')),
                ('tag_product', models.ManyToManyField(related_name='tag_product', to='main.TagProduct')),
            ],
        ),
    ]
