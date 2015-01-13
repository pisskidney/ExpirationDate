# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20150113_1520'),
        ('cemeteries', '0002_auto_20150113_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grave',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('receipt_number', models.BigIntegerField(verbose_name='receipt_number')),
                ('funeral_date', models.DateTimeField(verbose_name='funeral date')),
                ('surface_area', models.DecimalField(decimal_places=2, verbose_name='surface area', max_digits=5)),
                ('has_funeral_constructions', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='')),
                ('cemetery', models.ForeignKey(to='cemeteries.Cemetery')),
                ('deceased', models.ForeignKey(to='persons.Person')),
                ('owner', models.ForeignKey(related_name='graves', to='persons.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UpcomingFuneral',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('funeral_date', models.DateTimeField(verbose_name='funeral date')),
                ('date_added', models.DateTimeField(verbose_name='date added', auto_now_add=True)),
                ('deceased', models.ForeignKey(related_name='upcomming_funerals', to='persons.Person')),
                ('resting_place', models.ForeignKey(related_name='resting_places', to='cemeteries.RestingPlace')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
