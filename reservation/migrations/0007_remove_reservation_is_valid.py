# Generated by Django 3.2.16 on 2022-12-10 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_alter_reservation_tables'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='is_valid',
        ),
    ]