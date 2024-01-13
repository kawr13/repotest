# Generated by Django 4.2.6 on 2024-01-12 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CabinetApp', '0001_initial'),
        ('ProfileApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_teacher', to='ProfileApp.teacher'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cabinets', to='ProfileApp.teacher'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='users',
            field=models.ManyToManyField(related_name='cabinets', to=settings.AUTH_USER_MODEL),
        ),
    ]
