# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0007_auto_20150822_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilisation',
            name='birth_rate',
            field=models.FloatField(default=0.04),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='breeders',
            field=models.IntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='children',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='death_rate',
            field=models.FloatField(default=0.01),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='others',
            field=models.IntegerField(default=50),
        ),
    ]
