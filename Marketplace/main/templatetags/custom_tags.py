from django import template


register = template.Library()

@register.filter()
def revers_string(value):
    return value[::-1]