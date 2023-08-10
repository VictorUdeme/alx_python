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
         return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """Getter and setter for height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """Getter and setter for x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """Getter and setter for y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Adding the area
        this returns the value of height x width
        """
        return self.width * self.height
    
    def display(self):
        """
        Adding the display
        this displays the output"#"
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + '#' * self.width)

    def __str__(self):
        """
        adding the (str)
        this overides the str method so it returns:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
    
    def update(self, *args, **kwargs):
        """
        updated using using both:
        args and kwarks
        """
        if args:
            num = len(args)
            if num > 0:
                self.id = args[0]
            if num > 1:
                self.width = args[1]
            if num > 2:
                self.height = args[2]
            if num > 3:
                self.x = args[3]
            if num > 4:
                self.y = args[4]

        else:
            for key, value in kwargs.item():
                setattr(self, key, value)

        




