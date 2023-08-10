"""
check
"""
from models.base import Base

"""
Here, Reset the counter to start with id 1
"""
Base._Base__nb_objects = 0

b = Base()
if b is None or b.id != 1:
    exit(1)

exit(0)
