from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    teacher_id = models.OneToOneField('Teacher', on_delete=models.CASCADE)
    # requisites_id = models.OneToOneRel('Requisites', on_delete=models.CASCADE)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()

#
# class Requisites(models.Model):
#     card_number = models.CharField(max_length=16)
#     card_date = models.DateField()
#     card_cvv = models.CharField(max_length=3)
#

