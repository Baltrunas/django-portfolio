from django import template

from portfolio.models import Value


register = template.Library()


@register.filter(name='value')
def value(item, slug):
	value = Value.objects.get(image=item, property__slug=slug)
	return value
