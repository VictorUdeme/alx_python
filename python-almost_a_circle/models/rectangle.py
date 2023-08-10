"""
Importing from baseClass
"""


from models.base import Base

class Rectangle(Base):
    """Rectangle class"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Here, I called the super class with id
        """
        super().__init__(id)
        self.width = width
        self.height =height
        self.x = x
        self.y = y

    """Getter and setter for width"""
    @property
    def width(self):
         self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    """Getter and setter for height"""
    @property
    def height(self):
        self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    """Getter and setter for x"""
    @property
    def x(self):
        self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    """Getter and setter for y"""
    @property
    def y(self):
        self.__y

    @y.setter
    def y(self, value):
        self.__y = value



