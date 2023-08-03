class Square:
    """
This class defines a square by:

* Private instance attribute: size
* Instantiation with optional size (default 0)
* Size must be an integer, otherwise raise a TypeError exception with the message "size must be an integer"
* If size is less than 0, raise a ValueError exception with the message "size must be >= 0"
* Public instance method: def area(self): that returns the current square area

"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

