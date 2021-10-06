#!/usr/bin/python3
"""
Add integer function
Returns a + b
works with two integers
"""


def add_integer(a, b=98):
    """Function to add two integers
    checking if a and b are integers and
    are not float or boolean"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
