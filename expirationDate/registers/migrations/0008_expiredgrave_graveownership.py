# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_person_funeral_date'),
        ('registers', '0007_auto_20150115_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraveOwnership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expiration_date', models.DateField(verbose_name='expiration_date')),
                ('owned_grave', models.ForeignKey(related_name='owned_grave', to='registers.Grave')),
                ('person', models.ForeignKey(related_name='person', to='persons.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpiredGrave',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('registers.grave',),
        ),
    ]
