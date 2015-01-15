# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0006_graveownershiprequestsregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingFuneralArchive',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('registers.upcomingfuneral',),
        ),
        migrations.RemoveField(
            model_name='grave',
            name='funeral_date',
        ),
        migrations.AlterField(
            model_name='grave',
            name='deceased',
            field=models.ForeignKey(blank=True, to='persons.Person', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grave',
            name='receipt_number',
            field=models.BigIntegerField(null=True, verbose_name='receipt_number', blank=True),
            preserve_default=True,
        ),
    ]
