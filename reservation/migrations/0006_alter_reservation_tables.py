# Generated by Django 3.2.16 on 2022-12-10 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_reservation_is_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='tables',
            field=models.ManyToManyField(related_name='reservations', to='reservation.Table'),
        ),
    ]
