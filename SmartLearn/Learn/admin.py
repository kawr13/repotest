from django.contrib import admin
from django.contrib.admin import TabularInline
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from .models import *
# Register your models here.


class TagTabular(admin.TabularInline):
    model = Teacher.tags.through
    list_display = ('name',)
    extra = 0


@admin.register(Teacher)
class TeacherUsAdmin(admin.ModelAdmin):
    inlines = [TagTabular]
    list_display = ('description',)
    fields = ('description',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Requisites)
class RequisitesAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'card_date', 'card_cvv')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'first_name', 'last_name', 'phone_number', 'is_teacher', 'requisites')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('date_create',)


class ScheduleAdmin(TabularInline):
    model = Cabinet.schedules.through
    extra = 0


@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', 'teachers', 'users', 'schedules')
    inlines = [ScheduleAdmin]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_teacher')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_create', 'category', 'teacher', 'is_published', 'is_pinned', 'is_private')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'date_create', 'post', 'user')


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('url', 'teacher', 'date_create')
