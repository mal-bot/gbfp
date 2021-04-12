from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_age = models.IntegerField(verbose_name="Возраст", null=True, blank=True)
    user_about = models.TextField(verbose_name="О себе", null=True, blank=True)
    user_patronymic = models.CharField(verbose_name='Отчество', max_length=150, null=True, blank=True)
    company_name = models.CharField("Название компании", max_length=150, null=True, blank=True)
    company_about = models.TextField(verbose_name='О компании', null=True, blank=True)
    company_main_business = models.CharField("Род деятельности", max_length=150, null=True, blank=True)
    company_since = models.DateTimeField(verbose_name='Основана', null=True, blank=True)
    file = models.FileField(verbose_name='Фото', upload_to='avatars', blank=True)
    is_partner = models.BooleanField(verbose_name='Партнер', blank=True, default=False)


