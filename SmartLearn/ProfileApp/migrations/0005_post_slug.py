# Generated by Django 4.2.6 on 2024-01-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0004_service_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]