#!/usr/bin/python3
""" prints a square"""


def print_square(size):
    """prints a square

    Args:
        size (int): the size of the square to print

    Raises:
        TypeError
        ValueError

    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size <= 0:
        raise ValueError("size must be >= 0")
    if size == 0:
            print("")
    for i in range(size):
        print("#" * size, end="")
        print("")
