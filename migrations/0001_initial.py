# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('slug', models.SlugField(help_text='A slug is the part of a URL which identifies a page using human-readable keywords', max_length=128, verbose_name='\u042f\u0440\u043b\u044b\u043a')),
                ('description', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('order', models.PositiveSmallIntegerField(default=500, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('public', models.BooleanField(default=True, verbose_name='\u041f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044f')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u043e')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u043e')),
                ('sites', models.ManyToManyField(to='sites.Site', null=True, verbose_name='\u0421\u0430\u0439\u0442\u044b', blank=True)),
            ],
            options={
                'ordering': ['order', 'name'],
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u043f\u0440\u043e\u0435\u043a\u0442\u0430',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u043f\u0440\u043e\u0435\u043a\u0442\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('slug', models.SlugField(help_text='A slug is the part of a URL which identifies a page using human-readable keywords', max_length=128, verbose_name='\u042f\u0440\u043b\u044b\u043a')),
                ('logo', models.ImageField(upload_to=portfolio.models.upload_to, null=True, verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f', blank=True)),
                ('description', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('www', models.CharField(max_length=256, null=True, verbose_name='WWW', blank=True)),
                ('order', models.PositiveSmallIntegerField(default=500, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('public', models.BooleanField(default=True, verbose_name='\u041f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044f')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u043e')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u043e')),
                ('sites', models.ManyToManyField(to='sites.Site', null=True, verbose_name='\u0421\u0430\u0439\u0442\u044b', blank=True)),
            ],
            options={
                'ordering': ['order', 'name'],
                'verbose_name': '\u041a\u043b\u0438\u0435\u043d\u0442',
                'verbose_name_plural': '\u041a\u043b\u0438\u0435\u043d\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('slug', models.SlugField(help_text='A slug is the part of a URL which identifies a page using human-readable keywords', max_length=128, verbose_name='\u042f\u0440\u043b\u044b\u043a')),
                ('img', models.ImageField(upload_to=portfolio.models.upload_to, null=True, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True)),
                ('description', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('order', models.PositiveSmallIntegerField(default=500, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('public', models.BooleanField(default=True, verbose_name='\u041f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044f')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u043e')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u043e')),
            ],
            options={
                'ordering': ['order', 'name'],
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('slug', models.SlugField(help_text='A slug is the part of a URL which identifies a page using human-readable keywords', max_length=128, verbose_name='\u042f\u0440\u043b\u044b\u043a')),
                ('img', models.ImageField(upload_to=portfolio.models.upload_to, null=True, verbose_name='\u041e\u0431\u043b\u043e\u0436\u043a\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430', blank=True)),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('www', models.CharField(max_length=256, null=True, verbose_name='WWW', blank=True)),
                ('order', models.PositiveSmallIntegerField(default=500, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('main', models.BooleanField(default=False, verbose_name='\u041d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439')),
                ('public', models.BooleanField(default=True, verbose_name='\u041f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044f')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u043e')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u043e')),
                ('category', models.ForeignKey(related_name=b'category_project', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='portfolio.Category')),
                ('client', models.ForeignKey(verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442', blank=True, to='portfolio.Client', null=True)),
                ('sites', models.ManyToManyField(to='sites.Site', null=True, verbose_name='\u0421\u0430\u0439\u0442\u044b', blank=True)),
            ],
            options={
                'ordering': ['order', 'name'],
                'verbose_name': '\u041f\u0440\u043e\u0435\u043a\u0442',
                'verbose_name_plural': '\u041f\u0440\u043e\u0435\u043a\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('slug', models.SlugField(help_text='A slug is the part of a URL which identifies a page using human-readable keywords', max_length=128, verbose_name='\u042f\u0440\u043b\u044b\u043a')),
                ('img', models.ImageField(upload_to=portfolio.models.upload_to, null=True, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043e\u0442\u0437\u044b\u0432\u0430', blank=True)),
                ('text', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442', blank=True)),
                ('order', models.PositiveSmallIntegerField(default=500, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('public', models.BooleanField(default=True, verbose_name='\u041f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044f')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u043e')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u043e')),
                ('client', models.ForeignKey(related_name=b'client_reviews', verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442', to='portfolio.Client')),
                ('sites', models.ManyToManyField(to='sites.Site', null=True, verbose_name='\u0421\u0430\u0439\u0442\u044b', blank=True)),
            ],
            options={
                'ordering': ['order', 'name'],
                'verbose_name': '\u041e\u0442\u0437\u044b\u0432',
                'verbose_name_plural': '\u041e\u0442\u0437\u044b\u0432\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='project',
            field=models.ForeignKey(related_name=b'project_images', verbose_name='\u041f\u0440\u043e\u0435\u043a\u0442', to='portfolio.Project'),
            preserve_default=True,
        ),
    ]
