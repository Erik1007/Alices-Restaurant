# Generated by Django 3.2.16 on 2022-12-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0013_auto_20221216_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='name',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='start_time',
        ),
        migrations.AddField(
            model_name='reservation',
            name='booking_time',
            field=models.CharField(choices=[('1', '15:00-17:00'), ('2', '16:00-18:00'), ('3', '17:00-19:00'), ('4', '18:00-20:00'), ('5', '19:00-21:00'), ('6', '20:00-22:00')], default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='table',
            name='name',
            field=models.CharField(default='placeholder', max_length=50),
        ),
    ]
