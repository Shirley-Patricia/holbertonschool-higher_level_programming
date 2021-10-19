#!/usr/bin/python3
"""
Module of class Rectangle that inherits from class Base
"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle with privace instance attributes	with
    its own public getter and setter
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize attributes to describe a rectangle"""
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """the width property."""
        return self.__width

    @width.setter
    def width(self, width):
        """the setter method to store a new value in the attribute"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """the height property."""
        return self.__height

    @height.setter
    def height(self, height):
        """the setter method to store a new value in the attribute"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """the x property."""
        return self.__x

    @x.setter
    def x(self, x):
        """the setter method to store a new value in the attribute"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """the y property."""
        return self.__y

    @y.setter
    def y(self, y):
        """the setter method to store a new value in the attribute"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area calculated"""
        return (self.__width * self.__height)

    def display(self):
        """show figure rectangle with #"""
        for h in range(0, self.__y):
            print()
        space = ""
        for f in range(0, self.__x):
            space += " "
        s = ""
        for j in range(self.__width):
            s += "#"
        for i in range(self.__height):
            print(space + s)

    def __str__(self):
        """return a string"""
        text1 = "[Rectangle] ({}) {}/{}".format(self.id, self.x, self.y)
        text2 = " - {}/{}".format(self.width, self.height)
        return text1 + text2

    def update(self, *args, **kwargs):
        """Update the class Rectangle by adding the public method"""
        if len(args) >= 1:
            if len(args) == 1:
                self.id = args[0]

            if len(args) == 2:
                self.id = args[0]
                self.__width = args[1]

            if len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]

            if len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]

            if len(args) == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        # **kwargs must be skipped if *args exists and is not empty
        # Each key in this dictionary represents an attribute to the instance
        else:
            for key in kwargs.keys():
                if key == "id":
                    self.id = kwargs["id"]
                if key == "width":
                    self.width = kwargs["width"]
                if key == "height":
                    self.height = kwargs["height"]
                if key == "x":
                    self.x = kwargs["x"]
                if key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        dict_rectangle = {}
        dict_rectangle["id"] = self.id
        dict_rectangle["width"] = self.width
        dict_rectangle["height"] = self.height
        dict_rectangle["x"] = self.x
        dict_rectangle["y"] = self.y

        return dict_rectangle
