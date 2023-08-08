"""
BaseGeometry class
"""


BaseGeometry = __import__('5-base_geometry').BaseGeometry 
class Rectangle(BaseGeometry):
   
    """
        This class inherits from the BaseGeometry class and
        adds two private attributes: __width and __height
    """
    def __dir__(cls):
        # Call the parent class's __dir__ method to get the default attributes
       attributes = super().__dir__()
       return[item for item in attributes if item !="__init_subclass__"]
    
    def __init__(self, width, height):
        """
            The __init__() method of this subclass validate the 
            width and height perimeters
        """
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

        