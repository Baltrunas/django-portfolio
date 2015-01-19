# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20141107_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cover',
            field=models.ImageField(upload_to=apps.portfolio.models.category_upload_to, null=True, verbose_name='Cover', blank=True),
            preserve_default=True,
        ),
    ]
