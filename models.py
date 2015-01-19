# -*- coding: utf-8 -*
from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext as _


def file_type(filename):
	filename = filename.split('.')
	filetype = filename[len(filename) - 1].lower()
	return filetype


def client_upload_to(instance, filename):
	return 'portfolio/_clients/%s.%s' % (instance.slug, file_type(filename))

class Client(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))

	logo = models.ImageField(verbose_name=_('Logo'), upload_to=client_upload_to, blank=True, null=True)

	description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
	www = models.CharField(verbose_name=_('WWW'), max_length=256, blank=True, null=True)
	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500)

	sites = models.ManyToManyField(Site, verbose_name=_('Sites'), null=True, blank=True)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	@models.permalink
	def get_absolute_url(self):
		return ('portfolio_client', (), {'slug': self.slug})

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['order', 'name']
		verbose_name = _('Client')
		verbose_name_plural = _('Clients')


def category_upload_to(instance, filename):
	return 'portfolio/%s/_cover.%s' % (instance.slug, file_type(filename))

class Category(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))
	cover = models.ImageField(verbose_name=_('Cover'), upload_to=category_upload_to, blank=True, null=True)
	description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500)
	sites = models.ManyToManyField(Site, verbose_name=_('Sites'), null=True, blank=True)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	@models.permalink
	def get_absolute_url(self):
		return ('portfolio_category', (), {'slug': self.slug})

	def get_public_projects(self):
		return self.category_project.filter(public=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['order', 'name']
		verbose_name = _('Project Category')
		verbose_name_plural = _('Project Categories')


def cover_upload_to(instance, filename):
	return 'portfolio/%s/%s/_cover.%s' % (instance.category.slug, instance.slug, file_type(filename))

def icon_upload_to(instance, filename):
	return 'portfolio/%s/%s/_icon.%s' % (instance.category.slug, instance.slug, file_type(filename))

class Project(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	category = models.ForeignKey(Category, verbose_name=_('Category'), related_name='category_project')
	client = models.ForeignKey(Client, verbose_name=_('Client'), blank=True, null=True)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))

	cover = models.ImageField(verbose_name=_('Cover'), upload_to=cover_upload_to, blank=True, null=True)
	icon = models.ImageField(verbose_name=_('Icon'), upload_to=icon_upload_to, blank=True, null=True)
	description = models.TextField(verbose_name=_('Description'), blank=True)

	www = models.CharField(verbose_name=_('WWW'), max_length=256, blank=True, null=True)
	template = models.CharField(verbose_name=_('Template'), max_length=128, null=True, blank=True)
	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500)
	sites = models.ManyToManyField(Site, verbose_name=_('Sites'), null=True, blank=True)

	main = models.BooleanField(verbose_name=_('Main'), default=False)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	@models.permalink
	def get_absolute_url(self):
		return ('portfolio_project', (), {'category_slug': self.category.slug, 'project_slug': self.slug})

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['order', 'name']
		verbose_name = _('Project')
		verbose_name_plural = _('Projects')


def image_upload_to(instance, filename):
	return 'portfolio/%s/%s/%s.%s' % (instance.project.category.slug, instance.project.slug, instance.slug, file_type(filename))

class Image(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))
	project = models.ForeignKey(Project, verbose_name=_('Project'), related_name='project_images')

	img = models.ImageField(verbose_name=_('Image'), upload_to=image_upload_to, blank=True, null=True)
	description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['order', 'name']
		verbose_name = _('Image')
		verbose_name_plural = _('Images')


class Property(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	slug = models.SlugField(verbose_name=_('Slug'))
	unit = models.CharField(verbose_name=_('Unit'), max_length=32, blank=True)
	description = models.TextField(verbose_name=_('Description'), blank=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _('Property')
		verbose_name_plural = _('Properties')


class Value(models.Model):
	property = models.ForeignKey(Property, verbose_name=_('Property'), related_name='values')
	value = models.CharField(verbose_name=_('Value'), max_length=256)
	image = models.ForeignKey(Image, verbose_name=_('Image'), related_name='values')

	def __unicode__(self):
		return self.value

	class Meta:
		verbose_name = _('Value')
		verbose_name_plural = _('Values')


def review_upload_to(instance, filename):
	return 'portfolio/_review/%s.%s' % (instance.slug, file_type(filename))

class Review(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))

	client = models.ForeignKey(Client, verbose_name=_('Client'), related_name='client_reviews')

	img = models.ImageField(verbose_name=_('Review Image'), upload_to=review_upload_to, blank=True, null=True)

	text = models.TextField(verbose_name=_('Text'), blank=True, null=True)
	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500)
	sites = models.ManyToManyField(Site, verbose_name=_('Sites'), null=True, blank=True)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	@models.permalink
	def get_absolute_url(self):
		return ('portfolio_review', (), {'slug': self.slug})

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['order', 'name']
		verbose_name = _('Review')
		verbose_name_plural = _('Reviews')
