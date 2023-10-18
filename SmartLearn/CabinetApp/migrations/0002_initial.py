# Generated by Django 4.2.6 on 2023-10-17 12:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CabinetApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProfileApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabinet',
            name='teachers',
            field=models.ManyToManyField(related_name='cabinets', to='ProfileApp.teacher'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='users',
            field=models.ManyToManyField(related_name='cabinets', to=settings.AUTH_USER_MODEL),
        ),
    ]
