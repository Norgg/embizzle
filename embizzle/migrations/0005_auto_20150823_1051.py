# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0004_auto_20150823_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilisation',
            name='nutrient_production',
            field=models.IntegerField(default=10),
        ),
    ]
