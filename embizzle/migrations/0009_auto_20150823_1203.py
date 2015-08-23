# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0008_auto_20150823_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='palace_blocks',
            field=models.IntegerField(default=2),
        ),
    ]
