from django import template

# Create your custom tags and filters here

register = template.Library()


@register.simple_tag(takes_context=True)
def body_class(context):
    request = context['request']
    if request.path == '/':
        return 'index-page'
    elif request.path == '/blog/':
        return 'blog-page'
