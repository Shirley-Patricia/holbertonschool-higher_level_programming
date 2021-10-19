#!/usr/bin/python3
"""
Module of class Square that inherits from class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square  that inherits from Rectangle
    subclass from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize attributes to describe a square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """the width property."""
        return self.width

    @size.setter
    def size(self, size):
        """set the new value to size"""
        self.width = size
        self.height = size

    def __str__(self):
        """method should return [Square] (<id>) <x>/<y> - <size>
        - in our case, width or height
        """
        text1 = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        text2 = " - {}".format(self.width)
        return text1 + text2

    def update(self, *args, **kwargs):
        """Update the class Square by adding the public method """
        if len(args) >= 1:
            """enumerate() method adds counter to an iterable and returns it.
            The returned object is an enumerate object.
            You can convert enumerate objects to list and tuple using list()
            and tuple() method respectively."""
            for count, item in enumerate(args, 0):
                if count == 0:
                    self.id = item
                elif count == 1:
                    self.size = item
                elif count == 2:
                    self.x = item
                elif count == 3:
                    self.y = item
        else:
            for key in kwargs.keys():
                if key == "id":
                    self.id = kwargs["id"]
                if key == "size":
                    self.size = kwargs["size"]
                if key == "x":
                    self.x = kwargs["x"]
                if key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""

        dict_square = {}
        dict_square["id"] = self.id
        dict_square["size"] = self.size
        dict_square["x"] = self.x
        dict_square["y"] = self.y

        return dict_square
