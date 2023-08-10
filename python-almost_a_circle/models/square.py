"""
Importing from rectangle_class
"""


from models.rectangle import Rectangle
class Square:
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Here, I called the super class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overloading str
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
