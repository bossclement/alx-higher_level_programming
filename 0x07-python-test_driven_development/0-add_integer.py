#!/usr/bin/python3
"""0-add_integer.add_integer
This modules helps me add numbers, it has his function
"add_integer" that takes 2 arguments which can be float or
integer and hen the function returns their sum.
"""


def add_integer(a, b=98):
    """Returns:
        int: The sum of the 2 numbers.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if a == float("inf") or a == float("inf"):
        a = 0
    if b == float("inf") or b == float("inf"):
        b = 0
    return int(a) + int(b)
