# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0020_auto_20150823_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='tick_length',
            field=models.IntegerField(default=20),
        ),
    ]
