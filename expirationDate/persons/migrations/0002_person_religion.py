# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='religion',
            field=models.PositiveSmallIntegerField(verbose_name='gender', help_text='Indicates the religion of the user.', default=0, choices=[(0, 'Not specified'), (1, 'Christianity'), (2, 'Islam'), (3, 'Hinduism'), (4, 'Buddhism')]),
            preserve_default=True,
        ),
    ]
