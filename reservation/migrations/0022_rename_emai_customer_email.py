# Generated by Django 3.2.18 on 2023-05-09 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0021_auto_20230508_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='emai',
            new_name='email',
        ),
    ]
