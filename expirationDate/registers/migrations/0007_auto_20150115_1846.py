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
            model_name='upcomingfuneral',
            name='image',
        ),
        migrations.RemoveField(
            model_name='upcomingfuneral',
            name='resting_place',
        ),
        migrations.AddField(
            model_name='upcomingfuneral',
            name='grave',
            field=models.ForeignKey(related_name='grave', to='registers.Grave', default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='funeralmonument',
            name='location',
            field=models.ForeignKey(to='registers.Grave'),
            preserve_default=True,
        ),
    ]
