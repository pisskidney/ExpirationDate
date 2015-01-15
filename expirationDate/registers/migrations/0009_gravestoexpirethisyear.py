# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0008_expiredgrave_graveownership'),
    ]

    operations = [
        migrations.CreateModel(
            name='GravesToExpireThisYear',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('registers.grave',),
        ),
    ]
