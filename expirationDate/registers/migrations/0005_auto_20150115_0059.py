# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0004_auto_20150114_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualOwnerlessDeathRegister',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('registers.grave',),
        ),
        migrations.AddField(
            model_name='grave',
            name='social_services_request',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='IML request'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grave',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, related_name='graves', to='persons.Person'),
            preserve_default=True,
        ),
    ]
