# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0011_civilisation_recent_births'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilisation',
            name='birth_rate',
            field=models.FloatField(default=0.3),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='breeder_death_rate',
            field=models.FloatField(default=0.02),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='children_death_rate',
            field=models.FloatField(default=0.005),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='other_death_rate',
            field=models.FloatField(default=0.2),
        ),
    ]
