#!/usr/bin/python3
"""
Function that print a square
Returns nothing
works with character #
"""


def print_square(size):
    """Function to print square
    checking if size is integers and
    are not <0 or float"""

    if size == 0:
        print("")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
