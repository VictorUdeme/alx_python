"""BaseGeometry class"""
class BaseGeometry:
    """
    Base class for defining geometrical shapes and operations.

    This class serves as a foundation for creating specific geometrical shape classes
    with common attributes and methods related to geometry.
    """
    def __dir__(cls):
        return("This is dir for all class")

    attributes = super().__dir__()