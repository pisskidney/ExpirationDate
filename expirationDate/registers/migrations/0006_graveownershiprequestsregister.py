# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0005_auto_20150115_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraveOwnershipRequestsRegister',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('current_number', models.BigIntegerField(unique=True, verbose_name='current_number')),
                ('registration_date', models.DateTimeField(verbose_name='registration_date')),
                ('infocet_number', models.BigIntegerField(verbose_name='infocet_number')),
                ('status', models.PositiveSmallIntegerField(verbose_name='status', choices=[(0, 'Favorable'), (1, 'Not favorable'), (2, 'Partial'), (3, 'Rejected'), (4, 'Internal')], default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
