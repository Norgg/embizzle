# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='civilisation',
            name='population',
        ),
        migrations.AddField(
            model_name='civilisation',
            name='birth_rate',
            field=models.FloatField(default=0.001),
        ),
        migrations.AddField(
            model_name='civilisation',
            name='breeders',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='civilisation',
            name='children',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='civilisation',
            name='death_rate',
            field=models.FloatField(default=0.002),
        ),
        migrations.AddField(
            model_name='civilisation',
            name='others',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='civilisation',
            name='unrest',
            field=models.IntegerField(default=0),
        ),
    ]
