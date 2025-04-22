from django import template
from datetime import datetime

register = template.Library()

@register.filter
def format_datetime(dt_object):
    """Formats a datetime object as 'Mar 05, 2025, 14:30'."""
    if not dt_object:
        return 'N/A'
    # Ensure dt_object is a datetime object before formatting
    if isinstance(dt_object, datetime):
        return dt_object.strftime('%b %d, %Y, %H:%M')
    return str(dt_object) # Return as string if not a datetime object
