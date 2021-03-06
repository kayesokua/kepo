# Generated by Django 3.1.8 on 2021-05-02 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myjournal', '0003_delete_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eveningjournal',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='eveningjournal',
            name='question3',
        ),
        migrations.RemoveField(
            model_name='eveningjournal',
            name='question4',
        ),
        migrations.RemoveField(
            model_name='eveningjournal',
            name='question5',
        ),
        migrations.RemoveField(
            model_name='morningjournal',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='morningjournal',
            name='question1',
        ),
        migrations.RemoveField(
            model_name='morningjournal',
            name='question2',
        ),
        migrations.AddField(
            model_name='eveningjournal',
            name='q3a',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='eveningjournal',
            name='q3b',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='eveningjournal',
            name='q3c',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='eveningjournal',
            name='q4a',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='eveningjournal',
            name='q4b',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='eveningjournal',
            name='q4c',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='morningjournal',
            name='q1a',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='morningjournal',
            name='q1b',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='morningjournal',
            name='q1c',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='morningjournal',
            name='q2a',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='morningjournal',
            name='q2b',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='morningjournal',
            name='q2c',
            field=models.CharField(default='', max_length=200),
        ),
    ]
