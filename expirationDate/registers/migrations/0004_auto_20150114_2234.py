# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20150113_1520'),
        ('registers', '0003_auto_20150114_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualDeathIndexRegister',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('persons.person',),
        ),
        migrations.AddField(
            model_name='grave',
            name='parcel',
            field=models.SmallIntegerField(verbose_name='parcel', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grave',
            name='position',
            field=models.SmallIntegerField(verbose_name='position', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grave',
            name='row',
            field=models.SmallIntegerField(verbose_name='row', default=0),
            preserve_default=True,
        ),
    ]
