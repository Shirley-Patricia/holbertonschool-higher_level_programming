#!/usr/bin/python3
"""Write a function that returns the dictionary description 
with simple data structure for JSON serialization of an object
"""


import json


def class_to_json(obj):
    """json serialization of an object"""

    return json.dumps(obj.__dict__)
