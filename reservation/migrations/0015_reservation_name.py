# Generated by Django 3.2.16 on 2022-12-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0014_auto_20221217_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='name',
            field=models.CharField(default='unnamed', max_length=150),
            preserve_default=False,
        ),
    ]
