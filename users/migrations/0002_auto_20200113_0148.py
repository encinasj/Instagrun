# Generated by Django 3.0 on 2020-01-13 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='mofied',
            new_name='modified',
        ),
    ]
