from django.contrib.auth.models import AbstractUser
from django.db import models










class Cabinet(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(Teacher, related_name='cabinets')
    users = models.ManyToManyField(User, related_name='cabinets')
    schedules = models.ManyToManyField(Schedule, related_name='cabinets')

    def __str__(self):
        return self.name


# class CabinetUser(models.Model):
#     user = models.ManyToManyField(User, related_name='cabinet_user')
#     cabinet = models.OneToOneField('Cabinet', on_delete=models.CASCADE, related_name='user_cabinet')
#     date_create = models.DateTimeField(auto_now_add=True)
#
#
# class CabinetTeacher(models.Model):
#     teacher = models.ManyToManyField(Teacher, related_name='cabinet_teacher')
#     cabinet = models.OneToOneField('Cabinet', on_delete=models.CASCADE, related_name='teacher_cabinet')
#     date_create = models.DateTimeField(auto_now_add=True)


# class ServiceTeacher(models.Model):
#     teacher = models.ManyToManyField(Teacher, related_name='service_teacher')
#     cabinet = models.OneToOneField('Cabinet', on_delete=models.CASCADE, related_name='service_cabinet')
#     date_create = models.DateTimeField(auto_now_add=True)







# class CategoryTeacher(models.Model):
#     teacher = models.ManyToManyField(Teacher, related_name='category_teacher')
#     category = models.ManyToManyField(Category, related_name='category')







