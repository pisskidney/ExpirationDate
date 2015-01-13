# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20150113_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cemetery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='cemetery name', max_length=50)),
                ('address', models.CharField(verbose_name='address', max_length=200, blank=True)),
                ('postcode', models.CharField(verbose_name='postcode', max_length=10, blank=True, help_text='(e.g.:1234 AB)')),
                ('phone', models.CharField(verbose_name='phone', max_length=20, blank=True)),
                ('mobile', models.CharField(verbose_name='mobile', max_length=20, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RestingPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parcel', models.SmallIntegerField(verbose_name='parcel')),
                ('row', models.SmallIntegerField(verbose_name='row')),
                ('position', models.SmallIntegerField(verbose_name='position')),
                ('cemetery', models.ForeignKey(to='cemeteries.Cemetery', related_name='resting_places')),
                ('resident', models.ForeignKey(to='persons.Person', related_name='resting_places')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
