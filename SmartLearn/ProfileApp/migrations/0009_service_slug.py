# Generated by Django 4.2.6 on 2024-01-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0008_remove_service_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
