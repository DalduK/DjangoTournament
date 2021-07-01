# Generated by Django 3.2.4 on 2021-06-30 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_tournament_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='isOpen',
        ),
        migrations.AddField(
            model_name='tournament',
            name='closeDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
