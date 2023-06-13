#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file."""


import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"

save_to_json_file(sys.argv[1:], filename)
print(load_from_json_file(filename))
