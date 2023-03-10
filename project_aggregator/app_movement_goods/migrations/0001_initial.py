# Generated by Django 4.1.3 on 2023-02-04 23:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsideCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='Количество')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('delivery_type', models.CharField(choices=[('1', 'Обычная доставка'), ('2', 'Экспресс доставка')], default='1', max_length=1, verbose_name='Тип доставки')),
                ('payment_type', models.CharField(choices=[('1', 'Онлайн картой'), ('2', 'Онлайн со случайного чужого счета')], default='1', max_length=1, verbose_name='Тип оплаты')),
                ('card_number', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)], verbose_name='Номер карты')),
                ('delivery_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена доставки')),
                ('paid', models.BooleanField(default=False, verbose_name='оплачен')),
                ('status', models.CharField(blank=True, max_length=150, null=True, verbose_name='Ошибки оплаты')),
                ('payment_code', models.IntegerField(default=0, verbose_name='Код оплаты')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderContents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Содержание',
                'verbose_name_plural': 'Составы',
            },
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(default='', max_length=40, verbose_name='Сессия')),
                ('cart', models.ManyToManyField(blank=True, related_name='carts', through='app_movement_goods.InsideCart', to='app_products.product', verbose_name='Содержание корзины')),
            ],
            options={
                'verbose_name': 'Корзина пользователя',
                'verbose_name_plural': 'Корзины пользователей',
            },
        ),
    ]
