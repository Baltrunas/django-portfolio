# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='template',
            field=models.CharField(max_length=128, null=True, verbose_name='Template', blank=True),
            preserve_default=True,
        ),
    ]
