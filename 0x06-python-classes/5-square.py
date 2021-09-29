#!/usr/bin/python3
"""Define class"""


class Square:
    """Class square defined"""
    def __init__(self, size=0):
        """defined method"""
        self.__size = size
        """Private instance attribute"""

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """square area method"""
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
