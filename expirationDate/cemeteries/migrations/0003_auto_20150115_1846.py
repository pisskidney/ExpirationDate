# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0007_auto_20150115_1846'),
        ('cemeteries', '0002_auto_20150113_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restingplace',
            name='cemetery',
        ),
        migrations.RemoveField(
            model_name='restingplace',
            name='resident',
        ),
        migrations.DeleteModel(
            name='RestingPlace',
        ),
    ]
