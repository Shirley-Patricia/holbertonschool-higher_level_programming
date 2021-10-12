#!/usr/bin/python3
"""function returns True if the object is exactly an instance
of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    if a_class is object:
        return False
    if isinstance(obj, a_class):
        return True
    else:
        return False
