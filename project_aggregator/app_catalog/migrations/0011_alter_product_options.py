# Generated by Django 4.1.3 on 2023-01-25 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0010_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['price'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
