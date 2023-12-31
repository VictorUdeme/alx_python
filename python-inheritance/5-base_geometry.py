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
       return[item for item in attributes if item !="__init_subclass__"]
       
    


class BaseGeometry(metaclass=BaseGeometryMeta):
    """
    This class serves as a foundation for creating specific geometrical shape classes
    with common attributes and methods related to geometry.
    """
    def __dir__(cls):
        # Call the parent class's __dir__ method to get the default attributes
       attributes = super().__dir__()
       return[item for item in attributes if item !="__init_subclass__"]
    
    
    def area(self):
        """This raises an Exception error if area is not implemented"""
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """This method validates the value passed in.
        If the value is not an integer, 
           A TypeError exception is raised
        If the value is less than or equal to 0, 
           A ValueError exception is raised."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            
            raise ValueError(f"{name} must be greater than 0")

