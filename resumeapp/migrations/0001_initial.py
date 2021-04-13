# Generated by Django 3.1.7 on 2021-04-13 06:28

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
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Желаемая должность')),
                ('cellphone', models.PositiveBigIntegerField(verbose_name='Номер телефона')),
                ('salary', models.FloatField(blank=True, default=0, verbose_name='Ожидаемая заработная плата')),
                ('education', models.TextField(blank=True, default='', verbose_name='Образование')),
                ('job_list', models.TextField(blank=True, default='', verbose_name='Опыт работы')),
                ('key_words', models.TextField(blank=True, default='', verbose_name='Ключевы навыки')),
                ('languages', models.TextField(blank=True, default='', verbose_name='Знание языков')),
                ('is_draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_active', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Проверено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
                'ordering': ('resume_name',),
            },
        ),
    ]
