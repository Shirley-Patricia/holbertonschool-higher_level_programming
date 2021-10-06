#!/usr/bin/python3
"""
Function that print my name is <firs name> <lastname>
Returns nothing
works with strings
"""


def say_my_name(first_name, last_name=""):
    """The function say a name
    and checking if first name and last name are strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
