# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0002_funeralmonument'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingfuneral',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='funeralmonument',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grave',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
            preserve_default=True,
        ),
    ]
