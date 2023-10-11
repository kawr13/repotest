from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import *


# Register your models here.
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
