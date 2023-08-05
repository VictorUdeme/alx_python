"""
BaseGeometry class
"""

class BaseGeometryMeta(type):
     """
     Meta class for BaseGeometry
     """
     def __dir__(self):
        # Call the parent class's __dir__ method to get the default attributes
       attributes = super().__dir__()
       new_attribute = [item for item in attributes if item !="__init_subclass__"]
       return new_attribute
    


class BaseGeometry(metaclass=BaseGeometryMeta):
    """
    This class serves as a foundation for creating specific geometrical shape classes
    with common attributes and methods related to geometry.
    """
    def __dir__(self):
        # Call the parent class's __dir__ method to get the default attributes
       attributes = super().__dir__()
       new_attribute = [item for item in attributes if item !="__init_subclass__"]
       return new_attribute
    
    def area(self):
        """This raises an Exception error if area is not implemented"""
        raise Exception("area() is not implemented")
