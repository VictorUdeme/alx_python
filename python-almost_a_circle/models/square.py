"""
Importing from rectangle_class
"""


from models.rectangle import Rectangle
class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Here, I called the super class
        """
        super().__init__(size, size, x, y, id)

    """
    Getter and setter for width
    """
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overloading str
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
