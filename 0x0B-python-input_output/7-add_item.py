#!/usr/bin/python3
"""Load, add, save"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    list_json = load_from_json_file("add_item.json")
except FileNotFoundError:
    list_json = []
for i in sys.argv[1:]:
    list_json.append(i)
save_to_json_file(list_json, "add_item.json")
