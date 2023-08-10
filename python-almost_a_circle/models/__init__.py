"""
class import from base_class
"""
from models.base import Base

"""
Here, Reset the counter to start with id 1
"""
Base._Base__nb_objects = 0

"""
Creating an instance of Base without passing an id
"""
instance_without_id = Base()
