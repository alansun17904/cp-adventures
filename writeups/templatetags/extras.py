import re
import markdown
from django import template

cleaner = re.compile('<.*?>')
register = template.Library()


@register.filter(name='markdown')
def convert(value):
    return markdown.markdown(value)

@register.filter(name='preview')
def preview(value):
    value = re.sub(cleaner, '', value)
    return value if len(value) < 200 else value[0:200] + '...'