#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file."""


import sys
import json


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
with open(filename, encoding="utf-8", mode="a+") as f:
    f.close()

if len(sys.argv) < 2:
    sys.exit(0)

with open(filename) as f:
    old_data = json.load(f)

old_data = [*old_data, *sys.argv[1:]]
save_to_json_file(old_data, filename)
print(json.dumps(load_from_json_file(filename)))
