# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0010_civilisation_recent_deaths'),
    ]

    operations = [
        migrations.AddField(
            model_name='civilisation',
            name='recent_births',
            field=models.IntegerField(default=0),
        ),
    ]
