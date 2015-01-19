# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_category_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cover',
            field=models.ImageField(upload_to=apps.portfolio.models.cover_upload_to, null=True, verbose_name='Cover', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='icon',
            field=models.ImageField(upload_to=apps.portfolio.models.icon_upload_to, null=True, verbose_name='Icon', blank=True),
            preserve_default=True,
        ),
    ]
