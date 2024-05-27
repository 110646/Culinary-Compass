from django import template

register = template.Library()

@register.filter(name='half')
def half(value):
    try:
        return int(value) // 2
    except (ValueError, TypeError):
        return value