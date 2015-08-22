# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0009_auto_20150822_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilisation',
            name='breeder_death_rate',
            field=models.FloatField(default=0.02),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='breeders',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='children_death_rate',
            field=models.FloatField(default=0.01),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='other_death_rate',
            field=models.FloatField(default=0.04),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='others',
            field=models.IntegerField(default=20),
        ),
    ]
