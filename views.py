# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.template import RequestContext
from portfolio.models import Client
from portfolio.models import Review
from portfolio.models import Category
from portfolio.models import Project


def clients(request):
	context = {}
	context['clients'] = Client.objects.filter(public=True)
	context['title'] = _('Clients')
	return render_to_response('portfolio/clients.html', context, context_instance=RequestContext(request))


def client_detail(request, slug):
	context = {}
	context['client'] = get_object_or_404(Client, public=True, slug=slug)
	context['title'] = context['client'].name
	return render_to_response('portfolio/client_detail.html', context, context_instance=RequestContext(request))


def reviews(request):
	context = {}
	context['reviews'] = Review.objects.filter(public=True)
	context['title'] = _('Reviews')
	return render_to_response('portfolio/reviews.html', context, context_instance=RequestContext(request))


def portfolio(request):
	context = {}
	context['categories'] = Category.objects.filter(public=True)
	context['projects'] = Project.objects.filter(public=True)
	context['title'] = _('Categories')
	return render_to_response('portfolio/portfolio.html', context, context_instance=RequestContext(request))


def portfolio_category(request, slug):
	context = {}
	context['category'] = get_object_or_404(Category, public=True, slug=slug)
	context['projects'] = Project.objects.filter(public=True, category=context['category'])
	context['title'] = context['category'].name
	return render_to_response('portfolio/category.html', context, context_instance=RequestContext(request))


def portfolio_category_project(request, category_slug, project_slug):
	context = {}
	context['project'] = get_object_or_404(Project, public=True, slug=project_slug)
	context['title'] = context['project'].name
	return render_to_response('portfolio/project.html', context, context_instance=RequestContext(request))
