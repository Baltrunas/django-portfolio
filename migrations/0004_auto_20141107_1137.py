# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_property_value'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['name'], 'verbose_name': '\u0421\u0432\u043e\u0439\u0441\u0442\u0432\u043e', 'verbose_name_plural': '\u0421\u0432\u043e\u0439\u0441\u0442\u0432\u0430'},
        ),
        migrations.AlterModelOptions(
            name='value',
            options={'verbose_name': '\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435', 'verbose_name_plural': '\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f'},
        ),
        migrations.AlterField(
            model_name='project',
            name='template',
            field=models.CharField(max_length=128, null=True, verbose_name='\u0428\u0430\u0431\u043b\u043e\u043d', blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='unit',
            field=models.CharField(max_length=32, verbose_name='\u0411\u043b\u043e\u043a', blank=True),
        ),
        migrations.AlterField(
            model_name='value',
            name='property',
            field=models.ForeignKey(related_name=b'values', verbose_name='\u0421\u0432\u043e\u0439\u0441\u0442\u0432\u043e', to='portfolio.Property'),
        ),
        migrations.AlterField(
            model_name='value',
            name='value',
            field=models.CharField(max_length=256, verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435'),
        ),
    ]
