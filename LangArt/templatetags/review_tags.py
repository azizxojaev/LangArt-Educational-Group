from django import template

register = template.Library()

@register.filter
def times(number):
    """Возвращает range(number) для использования в for в шаблоне"""
    return range(number)

@register.filter
def remaining_stars(rating, max_stars=5):
    return range(max_stars - rating)
