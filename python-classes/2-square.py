"""
task 2, classes project
"""
class Square:
    """
This class defines a square by:




"""

    def __init__(self, size=0):
        """* Private instance attribute: size
           * Instantiation with optional size (default 0)
        """
        if not isinstance(size, int):
            """  If size is less than 0, raise a ValueError exception
                 with the message "size must be >= 0
            """
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method:
           def area(self): that returns the current square area
        """
        return self.__size * self.__size

