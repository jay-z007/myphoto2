# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0018_auto_20150920_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 9, 11, 38, 600945, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='time_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 9, 11, 38, 600945, tzinfo=utc)),
        ),
    ]
