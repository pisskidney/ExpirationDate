# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_person_religion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='religion',
            field=models.PositiveSmallIntegerField(help_text='Indicates the religion of the user.', default=0, choices=[(0, 'Not specified'), (1, 'Christianity'), (2, 'Islam'), (3, 'Hinduism'), (4, 'Buddhism')], verbose_name='religion'),
            preserve_default=True,
        ),
    ]
