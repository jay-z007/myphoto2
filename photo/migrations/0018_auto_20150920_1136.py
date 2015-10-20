# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0017_auto_20150920_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 6, 6, 4, 95531, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='time_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 6, 6, 4, 79904, tzinfo=utc)),
        ),
    ]
