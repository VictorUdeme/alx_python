"""
BaseGeometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry 

class Rectangle(BaseGeometry):
    """
    This class inherits from the BaseGeometry class and
    adds two private attributes: __width and __height
    """
    
    def __init__(self, width, height):
        """
        The __init__() method of this subclass validates the 
        width and height parameters
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle
        The area of a rectangle is calculated by: 
        multiplying the Width and Height
        """
        return self.__width * self.__height
    
    def __str__(self):
        """
        The __str__() method of the Rectangle class returns a string representation of the rectangle.
        It follows this format: [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
