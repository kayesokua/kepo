# Generated by Django 3.1.8 on 2021-04-26 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MorningJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('question1', models.TextField()),
                ('question2', models.TextField()),
                ('mood', models.IntegerField(choices=[(0, 'Neutral'), (1, 'Silly'), (2, 'Dreamy'), (3, 'Creative'), (4, 'Active')], default=0)),
                ('complete', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='morning_entries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EveningJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('question3', models.TextField()),
                ('question4', models.TextField()),
                ('question5', models.TextField()),
                ('mood', models.IntegerField(choices=[(0, 'Neutral'), (1, 'Silly'), (2, 'Dreamy'), (3, 'Creative'), (4, 'Active')], default=0)),
                ('complete', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evening_entries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
