# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(max_length=100, default='none'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(max_length=10, default='none'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(max_length=100, default='none'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='time_registered',
            field=models.TimeField(default=datetime.datetime(2015, 9, 19, 11, 3, 18, 548550, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
