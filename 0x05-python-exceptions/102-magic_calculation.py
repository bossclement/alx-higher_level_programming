#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError("i is greater than a")
            result += (a // i) + (b ** i)
        except Exception as e:
            result = b + a
            break
    return result
