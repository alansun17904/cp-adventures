import markdown
from django import template


register = template.Library()


@register.filter(name='markdown')
def convert(value):
    return markdown.markdown(value)

@register.filter(name='preview')
def preview(value):
    return value if len(value) < 200 else value[0:200] + '...'