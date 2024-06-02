from django import template

register = template.Library()

@register.filter(name='half')
def half(value):
    try:
        return int(value) // 2
    except (ValueError, TypeError):
        return value

@register.filter
def add_newlines(value):
    if not isinstance(value, str):
        return value
    # Split the text at each period followed by a space, then join with <br>
    return value.replace('.', '. ')

@register.filter
def fix_decimal_five(value):
    if not isinstance(value, str):
        return value
    return value.replace('. 5', '.5')

@register.filter
def is_essential_nutrient(nutrient_name):
    essential_nutrients = [
        "Calories", "Fat", "Protein", "Sodium", "Sugar", "Vitamin A", "Vitamin C",
        "Calcium", "Iron", "Vitamin D", "Vitamin E", "Vitamin K", "Vitamin B6",
        "Vitamin B12", "Magnesium", "Zinc"
    ]
    return nutrient_name in essential_nutrients