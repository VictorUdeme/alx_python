def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class"""
    #checking for if the object is an instance of the specified class
    if isinstance(obj, a_class):
        return True
    else:
        return False