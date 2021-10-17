#!/usr/bin/python3
""" 
My class module, project almost a circle
"""

class Base:
    """ first class or class base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
