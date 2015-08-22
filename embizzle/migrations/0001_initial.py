# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Civilisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Nowhere', max_length=1024)),
                ('funds', models.IntegerField(default=1000)),
                ('unrest', models.IntegerField(default=0)),
                ('children', models.IntegerField(default=0)),
                ('breeders', models.IntegerField(default=100)),
                ('others', models.IntegerField(default=20)),
                ('birth_rate', models.FloatField(default=0.04)),
                ('children_death_rate', models.FloatField(default=0.005)),
                ('breeder_death_rate', models.FloatField(default=0.01)),
                ('other_death_rate', models.FloatField(default=0.05)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('started_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_tick', models.DateTimeField(default=django.utils.timezone.now)),
                ('ticks', models.IntegerField(default=0)),
                ('tick_length', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Someone', max_length=1024)),
                ('funds', models.IntegerField(default=100)),
                ('civ', models.OneToOneField(related_name='leader', to='embizzle.Civilisation')),
                ('game', models.ForeignKey(related_name='leaders', to='embizzle.Game')),
                ('user', models.ForeignKey(related_name='leaders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
