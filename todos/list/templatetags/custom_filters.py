from django import template
import uuid

register = template.Library()

@register.filter(name='uuid_to_string')
def uuid_to_string(value):
    return str(value)
