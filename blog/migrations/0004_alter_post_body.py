# Generated by Django 3.2.18 on 2023-05-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default='Placeholder', max_length=250),
        ),
    ]