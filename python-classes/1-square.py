"""
task 0, classes project
"""
class Square:
    """
This class defines a square by:
* Instantiation with optional size: def __init__(self, size=0)

    """

    def __init__(self, size=0):
        '''* Private instance attribute: size
        * Instantiation with optional size: def __init__(self, size=0)
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    