# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0013_auto_20150823_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilisation',
            name='birth_rate',
            field=models.FloatField(default=0.2),
        ),
    ]
