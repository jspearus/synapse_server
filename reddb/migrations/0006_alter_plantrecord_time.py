# Generated by Django 4.1.7 on 2023-03-08 21:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reddb', '0005_rename_time_between_watering_plantdb_hours_between_watering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantrecord',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
