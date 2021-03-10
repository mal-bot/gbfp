from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    description = models.TextField("Описание", null=True, blank=True)
    age = models.IntegerField("Возраст", null=True, blank=True)
    about = models.TextField("О себе", null=True, blank=True)
    company_name = models.CharField("Название компании", max_length=150)
    main_business = models.CharField("Род деятельности", max_length=150)

# Create your models here.
# class Company(models.Model):
#     user = models.OneToOneField
#     name = models.CharField
#     description = models.CharField
#     since = models.DateTimeField
#     is_active = models.BooleanField
#     created_at = models.DateTimeField
#     edited_at = models.DateTimeField
#
#
# class Applicant(models.Model):
#     user = models.OneToOneField
#     first_name
