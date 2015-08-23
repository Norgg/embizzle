# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0007_auto_20150823_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='palace',
            field=models.CharField(default=b'                                                                                                                                                                                                                                                                ', max_length=256),
        ),
    ]
