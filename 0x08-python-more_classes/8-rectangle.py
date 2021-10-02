#!/usr/bin/python3
"""class rectangle created"""


class Rectangle:
    """empty class rectangle defined"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """defined method"""
        self.height = height
        self.width = width
        """Private instance attribute"""
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return ""
        var = ""
        for i in range(self.__height):
            for j in range(self.__width):
                var += str(self.print_symbol)
            if (self.__height - 1) != i:
                var += "\n"
        return var

    def __repr__(self):
        """return a string"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
