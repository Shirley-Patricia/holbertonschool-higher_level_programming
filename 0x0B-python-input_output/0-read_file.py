#!/usr/bin/python3
"""function read a text file
with open and print in stdout
"""


def read_file(filename=""):
    """using open to read file"""
    with open(filename, 'r') as file:
        print(file.read())
