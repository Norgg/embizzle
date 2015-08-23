# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0019_civilisation_total_deaths'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilisation',
            name='agriculture_level',
            field=models.IntegerField(default=17),
        ),
    ]
