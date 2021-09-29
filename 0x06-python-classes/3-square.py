#!/usr/bin/python3
"""Define class"""


class Square:
    """Class square defined"""
    def __init__(self, size=0):
        """defined method"""
        self.__size = size
        """Private instance attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """square area method"""
        return (self.__size ** 2)
