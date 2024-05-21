from django import template

# Create your custom template tags and filters here

register = template.Library()


@register.filter(name='persian_digits')
def persian_digits(value):
    translation_table = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
    return value.translate(translation_table)
