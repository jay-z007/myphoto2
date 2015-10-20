# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0009_auto_20150919_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='time_registered',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 9, 19, 12, 10, 17, 446710, tzinfo=utc)),
        ),
    ]
