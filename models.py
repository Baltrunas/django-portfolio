# -*- coding: utf-8 -*
from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext as _


def upload_to(instance, filename):
	file_type = filename.split('.')[len(filename.split('.')) - 1]
	puth = '%s/%s.%s' % (instance.dir_puth, instance.slug, file_type)
	return puth


class Client(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))

	dir_puth = 'img/portfolio/clients'
	logo = models.ImageField(verbose_name=_('Logo'), upload_to=upload_to, blank=True, null=True)

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


class Category(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))
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


class Project(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	category = models.ForeignKey(Category, verbose_name=_('Category'), related_name='category_project')
	client = models.ForeignKey(Client, verbose_name=_('Client'), blank=True, null=True)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))

	dir_puth = 'img/portfolio/project'
	img = models.ImageField(verbose_name=_('Project Image Cover'), upload_to=upload_to, blank=True, null=True)
	description = models.TextField(verbose_name=_('Description'), blank=True)
	# ?
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


class Image(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	#?
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))
	project = models.ForeignKey(Project, verbose_name=_('Project'), related_name='project_images')

	dir_puth = 'img/portfolio/screenshot'
	img = models.ImageField(verbose_name=_('Image'), upload_to=upload_to, blank=True, null=True)
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
		return self.name

	class Meta:
		verbose_name = _('Value')
		verbose_name_plural = _('Values')


class Review(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))

	client = models.ForeignKey(Client, verbose_name=_('Client'), related_name='client_reviews')

	dir_puth = 'img/portfolio/review'
	img = models.ImageField(verbose_name=_('Review Image'), upload_to=upload_to, blank=True, null=True)

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
