#!/usr/bin/python3
def print_last_digit(number):
    num = int(str(number)[-1])
    num = num * (-1 if number < 0 else 1)
    print(num, end="")
