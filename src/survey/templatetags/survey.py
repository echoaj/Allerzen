from django import template


def replace_underscores(value):
    value = value.replace('_', ' ')
    value = value.replace('and/or', 'and or')
    return value


register = template.Library()
register.filter('replace_', replace_underscores)