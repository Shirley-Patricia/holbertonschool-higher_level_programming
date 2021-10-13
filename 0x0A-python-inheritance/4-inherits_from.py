#!/usr/bin/python3
"""function returns True if the object is an instance of a class that inherited 
(directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """check inherance of class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
