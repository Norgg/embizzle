# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0008_auto_20150822_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='civilisation',
            name='death_rate',
        ),
        migrations.AddField(
            model_name='civilisation',
            name='breeder_death_rate',
            field=models.FloatField(default=0.002),
        ),
        migrations.AddField(
            model_name='civilisation',
            name='children_death_rate',
            field=models.FloatField(default=0.001),
        ),
        migrations.AddField(
            model_name='civilisation',
            name='other_death_rate',
            field=models.FloatField(default=0.004),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='breeders',
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='game',
            name='tick_length',
            field=models.IntegerField(default=1),
        ),
    ]
