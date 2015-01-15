# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0007_auto_20150115_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funeralmonument',
            name='deceased',
        ),
        migrations.RemoveField(
            model_name='funeralmonument',
            name='location',
        ),
        migrations.RemoveField(
            model_name='funeralmonument',
            name='owner',
        ),
        migrations.DeleteModel(
            name='FuneralMonument',
        ),
        migrations.CreateModel(
            name='FuneralMonument',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('registers.grave',),
        ),
    ]
