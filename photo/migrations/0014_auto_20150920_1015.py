# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0013_auto_20150920_0217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=60, null=True, blank=True)),
                ('image', models.ImageField(upload_to='images')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=50)),
                ('width', models.IntegerField(null=True, blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='users',
        ),
        migrations.AlterField(
            model_name='album',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 4, 45, 9, 989872, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='time_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 4, 45, 9, 989872, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='photo',
            name='albums',
            field=models.ManyToManyField(to='photo.Album', blank=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(to='photo.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
