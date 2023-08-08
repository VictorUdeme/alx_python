"""
BaseGeometry class
"""


Rectangle = __import__('7-rectangle').Rectangle
class Square(Rectangle):
    """
    This class inherits from the Rectangle class.
    """

    def __init__(self, size):
        """
        Here, The __init__() method of the Square
        class takes a single parameter: size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Implement the area method here as we did the previous.
        """
        return self.__size * self.__size
     