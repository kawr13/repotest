# Generated by Django 4.2.6 on 2024-01-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0006_service_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
