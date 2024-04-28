# filters.py

from django import template

register = template.Library()

@register.filter
def remove_b_prefix(value):
    
    return value[0]