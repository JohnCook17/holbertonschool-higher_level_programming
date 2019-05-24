#!/usr/bin/python3
""" adds ints """


def add_integer(a, b=98):
    """adds two ints

    Args:
        a: The first number.
        b: The second number.

    Returns:
        int: returns the sum of the two numbers.

    Raises:
        TypeError: Raises an exception

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
