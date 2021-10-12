#!/usr/bin/python3
"""function returns True if the object is exactly an instance
of the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """compare object with a specific class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
