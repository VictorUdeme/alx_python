"""
This describes the module
"""


def inherits_from(obj, a_class):
    """
    description for the method(function)
    """
    
    obj_class = type(obj)
    if issubclass(obj_class, a_class) and obj_class is not a_class:
        return True
    else:
        return False
