# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('embizzle', '0003_auto_20150822_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='tick_length',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='game',
            name='ticks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leader',
            name='civ',
            field=models.OneToOneField(related_name='leader', to='embizzle.Civilisation'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='game',
            field=models.ForeignKey(related_name='leaders', to='embizzle.Game'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='user',
            field=models.ForeignKey(related_name='leaders', to=settings.AUTH_USER_MODEL),
        ),
    ]
