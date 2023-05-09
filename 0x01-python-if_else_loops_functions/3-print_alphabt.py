#!/usr/bin/python3
for char in range(ord('a'), ord('z')+1):
    print("{}".format(chr(char)) if chr(char) not in "qe" else '\0', end="")
