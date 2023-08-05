"""
This is a module that contains a function to check if an object inherits from a given class.
"""

def inherits_from(obj, a_class):
    """
    Check if an object inherits from a given class.

    Parameters:
        obj (object): The object to check.
        a_class (class): The class to check against.

    Returns:
        bool: True if the object inherits from the class, False otherwise.
    """
    return issubclass(obj.__class__, a_class) and obj.__class__ is not a_class
