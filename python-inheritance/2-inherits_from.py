"""
task 2, inheritance Task
"""
def inherit_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited (directly or indirectly)
      from the specified class ; otherwise False.
    """
    if not isinstance(obj, type):
        raise TypeError("object must be an instance of a class")
    if a_class is obj.__class__:
        return True
    for base_class in obj.__class__.__base__:
        if inherit_from(base_class, a_class):
            return True
        else:
            return False