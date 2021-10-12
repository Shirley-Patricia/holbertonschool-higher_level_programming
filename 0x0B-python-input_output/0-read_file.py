#!/usr/bin/python3
"""function read a text file"""


def read_file(filename=""):
	with open(filename, 'r') as file:
		print(file.read())
