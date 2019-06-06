#!/usr/bin/python3
"""checks if inherits from class"""


def inherits_from(obj, a_class):
    """checks if inherits from class

    Args:
        obj: The object to compair
        a_class: The class to compair to

    Returns:
        bool: True
        bool: False

    """
    if not isinstance(obj, a_class) or not type(obj) is a_class:
        return True
    else:
        return False
