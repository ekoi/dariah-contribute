from django import template
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


register = template.Library()


@register.filter
def is_url(value):
    """Checks if the given value is a URL."""
    v = URLValidator()
    try:
        v(value)
    except ValidationError:
        return False
    return True
