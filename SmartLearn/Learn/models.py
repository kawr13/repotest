from django.contrib.auth.models import AbstractUser
from django.db import models


class Teacher(models.Model):
    description = models.TextField()


class Requisites(models.Model):
    card_number = models.CharField(max_length=16)
    card_date = models.DateField()
    card_cvv = models.CharField(max_length=3)


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    teacher = models.OneToOneField('Teacher', on_delete=models.CASCADE, related_name='user_teacher')
    requisites = models.OneToOneField('Requisites', on_delete=models.CASCADE, related_name='user_requisites')


class Schedule(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)


class Cabinet(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.OneToOneField('Schedule', on_delete=models.CASCADE, related_name='cabinet_schedule')


class CabinetUser(models.Model):
    user = models.ManyToManyField(User, related_name='cabinet_user')
    cabinet = models.OneToOneField('Cabinet', on_delete=models.CASCADE, related_name='user_cabinet')
    date_create = models.DateTimeField(auto_now_add=True)


class CabinetTeacher(models.Model):
    teacher = models.ManyToManyField(Teacher, related_name='cabinet_teacher')
    cabinet = models.OneToOneField('Cabinet', on_delete=models.CASCADE, related_name='teacher_cabinet')
    date_create = models.DateTimeField(auto_now_add=True)


class ServiceTeacher(models.Model):
    teacher = models.ManyToManyField(Teacher, related_name='service_teacher')
    cabinet = models.OneToOneField('Cabinet', on_delete=models.CASCADE, related_name='service_cabinet')
    date_create = models.DateTimeField(auto_now_add=True)


class Service(models.Model):
    name = models.CharField(max_length=100)
    service_teacher = models.ManyToManyField(Teacher, related_name='service_teacher')


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_teacher = models.ManyToManyField(Teacher, related_name='category_teacher')


class CategoryTeacher(models.Model):
    teacher = models.ManyToManyField(Teacher, related_name='category_teacher')
    category = models.ManyToManyField(Category, related_name='category')


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, related_name='post_category')
    teacher = models.ManyToManyField(Teacher, related_name='post_teacher')
    is_published = models.BooleanField(default=True)
    is_pinned = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)


class Comment(models.Model):
    content = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')


class Tag(models.Model):
    name = models.CharField(max_length=100)


class TeacherTag(models.Model):
    teacher = models.ManyToManyField(Teacher, related_name='teacher_tag')
    tag = models.ManyToManyField(Tag, related_name='tag_teacher')


class Record(models.Model):
    url = models.URLField()
    date_create = models.DateTimeField(auto_now_add=True)


class TeacherRecord(models.Model):
    teacher = models.ManyToManyField(Teacher, related_name='teacher_record')
    record = models.ManyToManyField(Record, related_name='record_teacher')
    date_create = models.DateTimeField(auto_now_add=True)