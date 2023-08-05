"""This functions takes two parameters"""
def inherits_from(obj, a_class):
    """Good"""
    return (issubclass(obj.__class__, a_class) and \
            obj.__class__ is not a_class)
