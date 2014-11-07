# -*- coding: utf-8 -*
from django.contrib import admin


from .models import Client
from .models import Review
from .models import Category
from .models import Project
from .models import Image
from .models import Property
from .models import Value


class ProjectInline(admin.StackedInline):
	model = Project
	extra = 0


class ReviewInline(admin.StackedInline):
	model = Review
	extra = 0


class ClientAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'www', 'order', 'public', 'created_at', 'updated_at']
	search_fields = ['name', 'slug', 'description', 'www', 'order', 'public', 'created_at', 'updated_at']
	list_editable = ['order', 'public']
	list_filter = ['public', 'created_at', 'updated_at']
	inlines = [ReviewInline, ProjectInline]

admin.site.register(Client, ClientAdmin)


class ReviewAdmin(admin.ModelAdmin):
	list_display = ['name', 'client', 'order', 'public', 'created_at', 'updated_at']
	search_fields = ['name', 'client', 'text', 'order', 'sites', 'public', 'created_at', 'updated_at']
	list_editable = ['order', 'public']
	list_filter = ['client', 'sites', 'public', 'created_at', 'updated_at']

admin.site.register(Review, ReviewAdmin)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'order', 'public', 'created_at', 'updated_at']
	search_fields = ['name', 'slug', 'description', 'order', 'sites', 'public', 'created_at', 'updated_at']
	list_editable = ['order', 'public']
	list_filter = ['sites', 'public', 'created_at', 'updated_at']

admin.site.register(Category, CategoryAdmin)


class ImageInline(admin.StackedInline):
	model = Image


class ProjectAdmin(admin.ModelAdmin):
	list_display = ['name', 'client', 'slug', 'www', 'order', 'public', 'created_at', 'updated_at']
	search_fields = ['name', 'client', 'slug', 'img', 'description', 'www', 'order', 'sites', 'public', 'created_at', 'updated_at']
	list_editable = ['order', 'public']
	list_filter = ['client', 'sites', 'public', 'created_at', 'updated_at']
	inlines = [ImageInline]

admin.site.register(Project, ProjectAdmin)


class ValueInline(admin.StackedInline):
	model = Value
	extra = 0

class ImageAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'project', 'order', 'public', 'created_at', 'updated_at']
	search_fields = ['name', 'slug', 'project', 'img', 'description', 'order', 'public', 'created_at', 'updated_at']
	list_editable = ['order', 'public']
	list_filter = ['project', 'public', 'created_at', 'updated_at']
	inlines = [ValueInline]

admin.site.register(Image, ImageAdmin)

admin.site.register(Property)

admin.site.register(Value)