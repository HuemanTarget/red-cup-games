# Generated by Django 3.0.3 on 2020-02-08 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200207_1310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
    ]
