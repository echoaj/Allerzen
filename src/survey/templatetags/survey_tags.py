from django import template


register = template.Library()


@register.filter
def remove_underscores(value):
    value = value.replace('_', ' ')
    value = value.replace('and_or', 'and/or')
    return value


register.filter('remove_', remove_underscores)

























'''
from django import template


register = template.Library()


@register.filter
def replace_underscores(value):
    value = value.replace("_", " ")
    return value.replace("and or", "and/or")


register.filter('replace_', replace_underscores)
'''