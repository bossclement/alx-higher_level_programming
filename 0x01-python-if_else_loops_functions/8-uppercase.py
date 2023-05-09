#!/usr/bin/python3
def uppercase(str):
    for char in str:
        dt = ord(char)
        if dt > 96 and dt < 123:
            dt += 32
        print("{}".format(chr(dt)))
    print("\n", end="")
