# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0005_game_started_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='name',
            field=models.CharField(default='Unknown', max_length=1024),
            preserve_default=False,
        ),
    ]
