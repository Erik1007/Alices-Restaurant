# Generated by Django 3.2.16 on 2022-12-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_auto_20221210_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
    ]
