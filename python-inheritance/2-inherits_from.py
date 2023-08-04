"""
task 2, inheritance Task
"""
def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Parameters:
        obj: Any - The object to check.
        a_class: type - The specified class to compare against.

    Returns:
        bool: True if the object is an instance of a subclass of the specified class; otherwise, False.
    """
    return issubclass(obj.__class__, a_class) and obj.__class__ is not a_class