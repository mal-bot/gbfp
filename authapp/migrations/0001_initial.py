# Generated by Django 3.1.7 on 2021-04-13 06:28

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_age', models.IntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('user_about', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('user_patronymic', models.CharField(blank=True, max_length=150, null=True, verbose_name='Отчество')),
                ('company_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Название компании')),
                ('company_about', models.TextField(blank=True, null=True, verbose_name='О компании')),
                ('company_main_business', models.CharField(blank=True, max_length=150, null=True, verbose_name='Род деятельности')),
                ('company_since', models.DateTimeField(blank=True, null=True, verbose_name='Основана')),
                ('file', models.FileField(blank=True, upload_to='avatars', verbose_name='Фото')),
                ('is_partner', models.BooleanField(blank=True, default=False, verbose_name='Партнер')),
                ('activation_key', models.CharField(blank=True, max_length=128)),
                ('activation_key_expires', models.DateTimeField(default=datetime.datetime(2021, 4, 15, 9, 28, 57, 620941), verbose_name='Актуальность ключа')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
