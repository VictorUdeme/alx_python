"""
This function takes two arguments: obj,
 which is the object you want to check, 
 and a_class, which is the specified class you want to compare against. 
 It will return True if obj is exactly an instance of the specified a_class,
 otherwise, it will return False.
"""
def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Parameters:
        obj: Any - The object to check.
        a_class: type - The specified class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class; otherwise, False.
    """
    return type(obj) is a_class
