# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('slug', models.SlugField(verbose_name='\u042f\u0440\u043b\u044b\u043a')),
                ('unit', models.CharField(max_length=32, verbose_name='Unit', blank=True)),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.SlugField(verbose_name='Value')),
                ('image', models.ForeignKey(related_name=b'values', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', to='portfolio.Image')),
                ('property', models.ForeignKey(related_name=b'values', verbose_name='Property', to='portfolio.Property')),
            ],
            options={
                'verbose_name': 'Value',
                'verbose_name_plural': 'Values',
            },
            bases=(models.Model,),
        ),
    ]
