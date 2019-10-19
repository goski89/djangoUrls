from django import template

register = template.Library()


@register.filter(name='cut_temp')
def cut_temp(value: str, arg):
    return value.replace(arg, '')


