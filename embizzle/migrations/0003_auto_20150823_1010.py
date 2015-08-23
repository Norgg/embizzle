# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0002_auto_20150823_0923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leader',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='leader',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='leader',
            name='deposed',
            field=models.BooleanField(default=False),
        ),
    ]
