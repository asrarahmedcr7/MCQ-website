from django import template
import logging
register = template.Library()

logger = logging.getLogger('django')

@register.filter
def get_item(dc, key):
    return dc.get(key)