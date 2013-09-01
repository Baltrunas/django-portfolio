# -*- coding: utf-8 -*
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('portfolio.views',
	# Clients
	url(r'^clients/$', 'clients', name='portfolio_clients'),

	# Client
	url(r'^clients/(?P<slug>[-_\d\w]+)/$', 'client', name='portfolio_client'),

	# Reviews
	url(r'^reviews/$', 'reviews', name='portfolio_reviews'),

	# Categories
	url(r'^portfolio/$', 'categories', name='portfolio_categories'),

	# Category
	url(r'^portfolio/(?P<slug>[-_\d\w]+)/$', 'category', name='portfolio_category'),

	# Project
	url(r'^portfolio/(?P<category_slug>[-_\d\w]+)/(?P<project_slug>[-_\d\w]+)/$', 'project', name='portfolio_project'),
)
