from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
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
