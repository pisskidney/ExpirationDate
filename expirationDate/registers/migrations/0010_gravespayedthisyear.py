# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0009_gravestoexpirethisyear'),
    ]

    operations = [
        migrations.CreateModel(
            name='GravesPayedThisYear',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('registers.grave',),
        ),
    ]
