# Generated by Django 3.0.2 on 2020-02-10 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_photo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='user',
        ),
    ]