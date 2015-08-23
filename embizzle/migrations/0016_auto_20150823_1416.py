# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0015_auto_20150823_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilisation',
            name='breeder_death_rate',
            field=models.FloatField(default=0.06),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='children_death_rate',
            field=models.FloatField(default=0.03),
        ),
    ]
