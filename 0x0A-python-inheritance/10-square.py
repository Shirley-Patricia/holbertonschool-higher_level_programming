#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass of rectangle"""
    def __init__(self, size):
        """sub method"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size