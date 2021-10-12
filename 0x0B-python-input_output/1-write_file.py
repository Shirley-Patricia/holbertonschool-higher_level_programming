#!/usr/bin/python3
"""function write a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """using open function"""
    with open(filename, 'w') as file:
        """return number of characters written in the file"""
        return file.write(text)
