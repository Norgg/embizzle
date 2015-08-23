# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0003_auto_20150823_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='civilisation',
            name='education_level',
        ),
        migrations.AddField(
            model_name='civilisation',
            name='nutrient_storage',
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='tax_rate',
            field=models.FloatField(default=0.3),
        ),
        migrations.AlterField(
            model_name='game',
            name='tick_length',
            field=models.IntegerField(default=30),
        ),
    ]
