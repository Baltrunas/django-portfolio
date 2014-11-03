# -*- coding: utf-8 -*
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _

from .models import Client
from .models import Review
from .models import Category
from .models import Project


def clients(request):
	context = {}
	context['clients'] = Client.objects.filter(public=True)
	context['title'] = _('Clients')
	return render(request, 'portfolio/clients.html', context)


def client(request, slug):
	context = {}
	context['client'] = get_object_or_404(Client, public=True, slug=slug)
	context['title'] = context['client'].name
	return render(request, 'portfolio/client.html', context)


def reviews(request):
	context = {}
	context['reviews'] = Review.objects.filter(public=True)
	context['title'] = _('Reviews')
	return render(request, 'portfolio/reviews.html', context)


def review(request, slug):
	context = {}
	context['review'] = get_object_or_404(Review, public=True, slug=slug)
	context['title'] = context['review'].name
	return render(request, 'portfolio/review.html', context)


def categories(request):
	context = {}
	context['categories'] = Category.objects.filter(public=True)
	# context['projects'] = Project.objects.filter(public=True)
	context['title'] = _('Categories')
	return render(request, 'portfolio/categories.html', context)


def category(request, slug):
	context = {}
	context['category'] = get_object_or_404(Category, public=True, slug=slug)
	context['projects'] = Project.objects.filter(public=True, category=context['category'])
	context['title'] = context['category'].name
	return render(request, 'portfolio/category.html', context)


def project(request, category_slug, project_slug):
	context = {}
	context['project'] = get_object_or_404(Project, public=True, slug=project_slug)
	context['title'] = context['project'].name
	return render(request, 'portfolio/project.html', context)
