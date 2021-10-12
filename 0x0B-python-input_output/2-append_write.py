#!/usr/bin/python3
"""function write at the end of a text file"""


def append_write(filename="", text=""):
    with open(filename, 'a') as file:
        return file.write(text)
