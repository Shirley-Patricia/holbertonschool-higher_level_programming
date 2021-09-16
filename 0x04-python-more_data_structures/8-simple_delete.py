#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key == "" or key != list(a_dictionary):
        return a_dictionary
    a_dictionary.deleted(key)
    return a_dictionary
