# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0010_auto_20150919_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='time_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 19, 12, 11, 46, 441900, tzinfo=utc)),
        ),
    ]
