# Generated by Django 4.2.6 on 2023-10-17 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('date_create', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CabinetApp.cabinet')),
            ],
        ),
    ]
