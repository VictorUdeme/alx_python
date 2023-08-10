"""
This defines BaseClass which would
be used for all future purpose.
"""


class Base:
    """
    This class keeps track of the number of instances created and assigns unique ids to them.
    """

    __nb_objects = 0
    
    
    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_objects
