# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20150113_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='funeral_date',
            field=models.DateTimeField(null=True, verbose_name='funeral date', blank=True),
            preserve_default=True,
        ),
    ]
