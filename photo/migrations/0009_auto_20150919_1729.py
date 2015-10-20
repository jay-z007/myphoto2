# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0008_auto_20150919_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='time_registered',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
