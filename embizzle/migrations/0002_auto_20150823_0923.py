# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilisation',
            name='tax_rate',
            field=models.FloatField(default=0.2),
        ),
    ]
