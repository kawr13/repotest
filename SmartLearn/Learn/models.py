from django.contrib.auth.models import AbstractUser
from django.db import models


class Cabinet(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(Teacher, related_name='cabinets')
    users = models.ManyToManyField(User, related_name='cabinets')
    schedules = models.ManyToManyField(Schedule, related_name='cabinets')

    def __str__(self):
        return self.name
