# Generated by Django 4.1.7 on 2023-03-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channeldata',
            name='id',
        ),
        migrations.AlterField(
            model_name='channeldata',
            name='ch_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plantrecord',
            name='humidity_lvl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plantrecord',
            name='light_lvl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plantrecord',
            name='moisture_lvl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plantrecord',
            name='temperature_lvl',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]