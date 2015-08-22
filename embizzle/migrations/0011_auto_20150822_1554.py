# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0010_auto_20150822_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilisation',
            name='breeder_death_rate',
            field=models.FloatField(default=0.01),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='children_death_rate',
            field=models.FloatField(default=0.005),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='other_death_rate',
            field=models.FloatField(default=0.05),
        ),
    ]
