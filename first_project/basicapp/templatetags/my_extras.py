from django import template

# custom filter 
register = template.library() 

@register.filter('cut')

def cut(value, arg):
    """
    This couts out al values of 'arg' from the string! 
    """
    return value.replace(arg, '') 

# custom filter register 
# register.filter('cut', cut)