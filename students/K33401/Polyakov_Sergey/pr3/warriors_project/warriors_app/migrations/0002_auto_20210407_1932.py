# Generated by Django 3.1.7 on 2021-04-07 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warriors_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='warrior',
            old_name='skill',
            new_name='skills',
        ),
    ]
