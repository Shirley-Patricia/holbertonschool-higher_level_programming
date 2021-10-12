#!/usr/bin/python3
"""function returns True if the object is exactly an instance
of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """compare object with a specific class"""
    
    if type(obj) is a_class:
        return True
    else:
        return False
