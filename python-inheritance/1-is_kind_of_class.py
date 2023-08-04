"""
task 1, inheritance Task
"""

def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, 
    or if the object is an instance of a class that 
    inherited from, the specified class ; otherwise False.
    """
    # Check if the object is an instance of the specified class.
    if isinstance(obj, a_class):
     return True
    # Check if the object is an instance of a class that inherited from the specified class.
    while hasattr(a_class, '__bases__'):
     if isinstance(obj, a_class.__bases__):
      return True
     a_class = a_class.__bases__[0]
    # If the object is not an instance of the specified class or any of its subclasses, return False.
    return False


