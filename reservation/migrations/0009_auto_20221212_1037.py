# Generated by Django 3.2.16 on 2022-12-12 10:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_auto_20221212_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 12, 10, 37, 58, 860493, tzinfo=utc), verbose_name='Start time'),
        ),
    ]