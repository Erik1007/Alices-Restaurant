# Generated by Django 3.2.18 on 2023-05-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230522_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default='', help_text='Enter your post content here', max_length=250),
        ),
    ]