#!/usr/bin/python3
char = 122
prev = 1
while char > 96:
    result = char
    if prev % 2 == 0:
        result -= 32
    print("{}".format(chr(result)), end="")
    prev += 1
    char -= 1
