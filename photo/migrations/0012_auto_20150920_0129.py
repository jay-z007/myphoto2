# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0011_auto_20150919_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('album_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cover_photo', models.ImageField(upload_to='covers')),
                ('upload_time', models.DateTimeField(default=datetime.datetime(2015, 9, 19, 19, 59, 58, 381967, tzinfo=utc))),
            ],
            options={
                'ordering': ('album_name',),
            },
        ),
        migrations.AlterField(
            model_name='myuser',
            name='time_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 19, 19, 59, 58, 381967, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='album',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
