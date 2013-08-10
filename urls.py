# -*- coding: utf-8 -*
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('portfolio.views',
	# Clients
	url(r'^clients/$', 'clients', name='portfolio_clients'),

	# Client
	url(r'^clients/(?P<slug>[-_\d\w]+)/$', 'client_detail', name='portfolio_client_detail'),

	# Review
	url(r'^reviews/$', 'reviews', name='portfolio_reviews'),

	url(r'^portfolio/$', 'portfolio', name='portfolio_portfolio'),
	url(r'^portfolio/(?P<slug>[-_\d\w]+)/$', 'portfolio_category', name='portfolio_portfolio_category'),
	url(r'^portfolio/(?P<category_slug>[-_\d\w]+)/(?P<project_slug>[-_\d\w]+)/$', 'portfolio_category_project', name='portfolio_portfolio_category_project'),
)
