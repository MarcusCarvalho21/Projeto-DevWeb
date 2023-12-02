from django import template
import base64

register = template.Library()

@register.filter
def base64_encode(value):
    return base64.b64encode(str(value).encode('utf-8')).decode('utf-8')