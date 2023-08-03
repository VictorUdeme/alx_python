class Square:
    """
This class defines a square by:

* Private instance attribute: size
* Instantiation with size (no type/value verification)

You are not allowed to import any module.
"""

    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size
    