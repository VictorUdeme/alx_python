"""
task 2, inheritance Task
"""

  # Good
def inherits_from(obj, a_class):
    return issubclass(obj.__class__, a_class) and obj.__class__ is not a_class