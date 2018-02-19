from django import template

register = template.Library()


@register.filter(name='coupe')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('coupe',cut)
