# Generated by Django 4.1.3 on 2023-01-27 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_movement_goods', '0007_rename_goods_insidecart_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='session',
            field=models.CharField(default='', max_length=40, verbose_name='Сессия'),
        ),
    ]