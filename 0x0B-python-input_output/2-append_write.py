#!/usr/bin/python3
"""that appends a string at the end of a text file(UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """open file and append text"""
    with open(filename, 'a') as file:
        return file.write(text)
