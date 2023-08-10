#!/usr/bin/python3
""" Check """
try:
    from models.base import Base

    """
    Resetting the counter to start with id 1
    """
    Base._Base__nb_objects = 0

    instance = Base()
    if instance.id != 1:
        exit(1)

    exit(0)
except ImportError:
    pass
