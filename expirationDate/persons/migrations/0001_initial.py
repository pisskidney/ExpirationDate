# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(verbose_name='first name', max_length=50)),
                ('last_name', models.CharField(verbose_name='last name', max_length=50)),
                ('birth_date', models.DateField(verbose_name='birth date', null=True, blank=True)),
                ('date_of_death', models.DateField(verbose_name='date of death', null=True, blank=True)),
                ('birth_place', models.CharField(verbose_name='birth place', blank=True, max_length=100)),
                ('address', models.CharField(verbose_name='address', blank=True, max_length=200)),
                ('postcode', models.CharField(verbose_name='postcode', help_text='(e.g.:1234 AB)', blank=True, max_length=10)),
                ('phone', models.CharField(verbose_name='phone', blank=True, max_length=20)),
                ('mobile', models.CharField(verbose_name='mobile', blank=True, max_length=20)),
                ('gender', models.PositiveSmallIntegerField(verbose_name='gender', choices=[(0, 'Not specified'), (1, 'Male'), (2, 'Female')], help_text='Indicates the gender of the user.', default=0)),
                ('is_deceased', models.BooleanField(verbose_name='is deceased', default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
