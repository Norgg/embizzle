# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0002_auto_20150822_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_tick', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='civilisation',
            name='funds',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='leader',
            name='game',
            field=models.ForeignKey(default=0, to='embizzle.Game'),
            preserve_default=False,
        ),
    ]
