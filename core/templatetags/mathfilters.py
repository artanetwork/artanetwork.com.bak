from django import template

# Create your custom template tags and filters here

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    return value * arg
