#!/usr/bin/python3
"""checks if is the same class"""


def is_same_class(obj, a_class):
    """checks if is the same class

    Args:
        obj: the object to check
        a_class: the class to check against

    Returns:
        bool: True if it is of the same class
        bool: False if it is not of the same class

    """
    if type(obj) is a_class:
        return True
    else:
        return False
