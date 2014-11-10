from django import template

from ..models import Value


register = template.Library()


@register.filter(name='value')
def value(item, slug):
	try:
		value = Value.objects.get(image=item, property__slug=slug)
		return value
	except:
		return ''
