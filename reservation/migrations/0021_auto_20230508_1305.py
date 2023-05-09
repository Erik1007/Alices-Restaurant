# Generated by Django 3.2.18 on 2023-05-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0020_auto_20230503_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emai', models.EmailField(max_length=200)),
                ('number_of_persons', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=200),
        ),
    ]