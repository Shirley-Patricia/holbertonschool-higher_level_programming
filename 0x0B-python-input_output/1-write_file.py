#!/usr/bin/python3
"""function write a text file"""


def write_file(filename="", text=""):
    with open(filename, 'w') as file:
        return file.write(text)
