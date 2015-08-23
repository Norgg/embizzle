# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0016_auto_20150823_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilisation',
            name='birth_rate',
            field=models.FloatField(default=0.25),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='nutrients',
            field=models.IntegerField(default=500),
        ),
        migrations.AlterField(
            model_name='game',
            name='tick_length',
            field=models.IntegerField(default=1),
        ),
    ]
