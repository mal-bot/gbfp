# Generated by Django 3.1.7 on 2021-04-14 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Наименование должности')),
                ('description', models.TextField(blank=True, max_length=250, null=True, verbose_name='Описание должности')),
                ('salary', models.FloatField(blank=True, default=0, verbose_name='Заработная плата')),
                ('is_draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('is_active', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлена')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Проверено')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ('-created_at',),
            },
        ),
    ]
