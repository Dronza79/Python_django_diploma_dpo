# Generated by Django 4.1.3 on 2023-01-16 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0006_alter_propertyproduct_device_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='titleproperty',
            options={'verbose_name': 'Свойство', 'verbose_name_plural': 'Свойства'},
        ),
    ]
