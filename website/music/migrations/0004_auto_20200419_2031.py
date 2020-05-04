# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0003_auto_20200419_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='file_type',
        ),
        migrations.AddField(
            model_name='album',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default=b'', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_title',
            field=models.CharField(max_length=250),
        ),
    ]
