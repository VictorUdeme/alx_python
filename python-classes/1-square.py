class Square:
    """
This class defines a square by:

* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0)

You are not allowed to import any module.
"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    