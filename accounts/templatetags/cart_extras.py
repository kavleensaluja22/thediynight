from django import template

register = template.Library()

@register.filter
def sum_prices(cart_items, method_name):
    total = 0
    for item in cart_items:
        method = getattr(item, method_name)
        total += method() if callable(method) else method
    return total
