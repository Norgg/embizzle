# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0011_auto_20150822_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='tick_length',
            field=models.IntegerField(default=5),
        ),
    ]
