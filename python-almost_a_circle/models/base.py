"""
This defines BaseClass which would
be used for all future purpose.
"""


class Base:
    """
    Base class to manage the id attribute for all future classes.
    
    This class keeps track of the number of instances created and assigns unique ids to them.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        
        Args:
            id (int, optional): If provided, assigns the given id to the instance. If not provided,
                               increments the internal counter and assigns a new unique id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

