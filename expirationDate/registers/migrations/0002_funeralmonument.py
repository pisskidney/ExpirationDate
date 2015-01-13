# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cemeteries', '0002_auto_20150113_1729'),
        ('persons', '0003_auto_20150113_1520'),
        ('registers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuneralMonument',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('receipt_number', models.BigIntegerField(verbose_name='receipt_number')),
                ('funeral_date', models.DateTimeField(verbose_name='funeral date')),
                ('surface_area', models.DecimalField(verbose_name='surface area', max_digits=5, decimal_places=2)),
                ('has_funeral_constructions', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='')),
                ('deceased', models.ForeignKey(related_name='funeral_monuments', to='persons.Person')),
                ('location', models.ForeignKey(to='cemeteries.RestingPlace')),
                ('owner', models.ForeignKey(to='persons.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
