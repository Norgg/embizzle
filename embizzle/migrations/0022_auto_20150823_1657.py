# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0021_auto_20150823_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilisation',
            name='funds',
            field=models.FloatField(default=300.0),
        ),
    ]
