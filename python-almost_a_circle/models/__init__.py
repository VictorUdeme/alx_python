"""
imports from base class
"""
from models.base import Base

"""
Creating an instance of Base without passing an id
"""
instance_without_id = Base()

"""
Accessing the id attribute of the instance
"""
print("Instance id:", instance_without_id.id)
