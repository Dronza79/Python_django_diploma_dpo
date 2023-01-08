# Generated by Django 4.1.3 on 2023-01-08 19:54

import app_users.managers
import app_users.models
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyGroups',
            fields=[
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$')], verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('username', models.CharField(blank=True, default='', max_length=30, verbose_name='Никнейм')),
                ('second_name', models.CharField(blank=True, default='', max_length=30, verbose_name='Отчество')),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/', validators=[app_users.models.User.validate_size, django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'], message='Расширение не поддерживается. Разрешенные расширения .jpg .gif .png')], verbose_name='Ссылка на изображение')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['id'],
            },
            managers=[
                ('objects', app_users.managers.UserManager()),
            ],
        ),
    ]
