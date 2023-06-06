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

    a = a if type(a) is not float else int(a)
    b = b if type(b) is not float else int(b)

    return (a + b)
