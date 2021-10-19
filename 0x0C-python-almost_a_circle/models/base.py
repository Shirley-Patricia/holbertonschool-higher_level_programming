#!/usr/bin/python3
"""
My class module, project almost a circle
"""


class Base:
    """ first class: class base
    __nb_objects is a private class attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor, 
        initiation of the class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        """integer validation of attributes of rectangle"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            if name == width or name == height:
                raise ValueError("{} must be > 0".format(name))
        if value < 0:
            if name == x or name == y:
                raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionariesn is None or list_dictionaries == []:
            return "[]"
        else:
            return
            json.dump(list_dictionaries)

    """ def save_to_file(cls, list_objs):"""
