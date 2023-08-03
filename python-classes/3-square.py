"""
task 3, classes project
"""
class Square:
    def __init__(self, size=0):
        '''
        Initialize a square instance with an optional size.
        Args:
            size (int): The size of the square side (default is 0)
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        '''
        self.__size = size
    
    @property
    def size(self):
        '''Getter method to retrieve the size of the square
        
           Returns:
                int: The size of the square side.
        '''
        return self.__size
    
    @size.setter
    def size(self, value):
        '''
        Used Setter method to set the size of the square.
        
        Args:
            value(int): The new size of the square side.
        
        Raises:
            TypeError: If the new size is not an integer.
            ValueError: If the new size is less than 0
            
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        return self.__size ** 2