# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20150919_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='time_registered',
            field=models.TimeField(default=datetime.datetime(2015, 9, 19, 11, 16, 34, 814274, tzinfo=utc)),
        ),
    ]
