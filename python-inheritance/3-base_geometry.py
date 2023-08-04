"""BaseGeometry class"""
class BaseGeometry:
    """
    This class serves as a foundation for creating specific geometrical shape classes
    with common attributes and methods related to geometry.
    """
    def __dir__(cls) -> None:
        attrbutes = super().__dir__()
        n_attributes = []
        for attr in attrbutes:
            if attr != '__init_subclass__':
                n_attributes.append(attr)
        return n_attributes
