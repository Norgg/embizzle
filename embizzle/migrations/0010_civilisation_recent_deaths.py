# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0009_auto_20150823_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='civilisation',
            name='recent_deaths',
            field=models.IntegerField(default=0),
        ),
    ]
