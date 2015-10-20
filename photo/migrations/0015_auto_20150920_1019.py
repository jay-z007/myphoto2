# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0014_auto_20150920_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='album',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 4, 49, 6, 775377, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='time_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 4, 49, 6, 775377, tzinfo=utc)),
        ),
    ]
