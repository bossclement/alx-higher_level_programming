#!/usr/bin/python3
import imp
import sys

# Load the compiled module
module = imp.load_compiled("hidden_4", "hidden_4.pyc")

# Get all the names defined in the module
names = [name for name in dir(module) if not name.startswith("__")]

# Sort the names alphabetically and print them
for name in sorted(names):
    print(name)
