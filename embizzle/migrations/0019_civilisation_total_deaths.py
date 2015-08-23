# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0018_auto_20150823_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='civilisation',
            name='total_deaths',
            field=models.IntegerField(default=0),
        ),
    ]
