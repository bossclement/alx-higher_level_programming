#!/usr/bin/python3
"""0-add_integer.add_integer
This modules helps me add numbers, it has his function
"add_integer" that takes 2 arguments which can be float or
integer and hen the function returns their sum.
"""


def add_integer(a, b=98):
    """Adds 2 numbers.
    Args:
        a (int): first number.
        b (int): second number.
    Returns:
        int: The sum of the 2 numbers.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
