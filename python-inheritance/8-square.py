"""BaseGeometry class(SuperClass)"""
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
    def __dir__(self):
        # Call the parent class's __dir__ method to get the default attributes
       attributes = super().__dir__()
       new_attribute = [item for item in attributes if item !="__init_subclass__"]
       return new_attribute
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

class Rectangle(BaseGeometry):
   
    """
        This class inherits from the BaseGeometry class and
        adds two private attributes: __width and __height
    """
    def __dir__(self):
        # Call the parent class's __dir__ method to get the default attributes
       attributes = super().__dir__()
       new_attribute = [item for item in attributes if item !="__init_subclass__"]
       return new_attribute
    def __init__(self, width, height):
        """
        The init method
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        This Area the area of the instance
        """
        return self.__width * self.__height
    
    def __str__(self):
        """str magic method """
        return f"[Rectangle] {self.__width}/{self.__height}"
    
    def __repr__(self):
        """The repr magic method """ 
        return f"Rectangle{self.__width}, {self.__height}"
    

class square():
    def __init__(self, size):
        self.__size =super().integer_validator("size", size)
        super().__init__(size)
       
