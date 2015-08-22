# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0004_auto_20150822_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='started_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
