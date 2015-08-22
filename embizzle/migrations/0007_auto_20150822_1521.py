# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0006_leader_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilisation',
            name='birth_rate',
            field=models.FloatField(default=0.004),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='death_rate',
            field=models.FloatField(default=0.001),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='name',
            field=models.CharField(default=b'Nowhere', max_length=1024),
        ),
        migrations.AlterField(
            model_name='leader',
            name='funds',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='leader',
            name='name',
            field=models.CharField(default=b'Someone', max_length=1024),
        ),
    ]
