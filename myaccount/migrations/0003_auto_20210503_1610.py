# Generated by Django 3.1.8 on 2021-05-03 16:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myaccount', '0002_auto_20210503_1238'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='UserProfile',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='birthdate',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='location',
            new_name='loc',
        ),
    ]