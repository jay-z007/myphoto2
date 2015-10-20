# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20150919_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='time_registered',
            field=models.TimeField(default=datetime.datetime(2015, 9, 19, 11, 24, 47, 355359, tzinfo=utc)),
        ),
    ]
