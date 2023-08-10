"""
This defines BaseClass which would
be used for all future purpose.
"""


class Base:
    """Base class for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the object."""
        
        if id is not None:
            self.id = id
        else:
            """Increment __nb_objects"""
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
