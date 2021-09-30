#!/usr/bin/python3
"""class rectangle created"""


class Rectangle:
    """empty class rectangle defined"""
    def __init__(self, width=0, height=0):
        """defined method"""
        self.height = height
        self.width = width
        """Private instance attribute"""

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2 + self.__height * 2)

    def __str__(self) -> str:
        var = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                var += "#"
            if (self.__height - 1) != i:
                var += "\n"
        return var

    def __repr__(self):
        return ("Rectangle ({:d}, {:d})".format(self.__width, self.__height))
