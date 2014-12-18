from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^clients/$', views.clients, name='portfolio_clients'),
	url(r'^clients/(?P<slug>[-_\d\w]+)/$', views.client, name='portfolio_client'),
	url(r'^reviews/$', views.reviews, name='portfolio_reviews'),
	url(r'^reviews/(?P<slug>[-_\d\w]+)/$', views.review, name='portfolio_review'),
	url(r'^portfolio/$', views.categories, name='portfolio_categories'),
	url(r'^portfolio/(?P<slug>[-_\d\w]+)/$', views.category, name='portfolio_category'),
	url(r'^portfolio/(?P<category_slug>[-_\d\w]+)/(?P<project_slug>[-_\d\w]+)/$', views.project, name='portfolio_project'),
]
