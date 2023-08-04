"""
This function takes two arguments: obj,
 which is the object you want to check, 
 and a_class, which is the specified class you want to compare against. 
 It will return True if obj is exactly an instance of the specified a_class,
 otherwise, it will return False.
"""
def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if it's an instance of a class that inherited from, the specified class.

    Parameters:
        obj: Any - The object to check.
        a_class: type - The specified class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class or its subclass; otherwise, False.
    """
    return isinstance(obj, a_class)