#!/usr/bin/python3
"""checks if is the same class"""


def is_kind_of_class(obj, a_class):
    """checks if is the same kind of class

    Args:
        obj: the object to check
        a_class: the class to check against

    Returns:
        bool: True if it is an obj of the class False otherwise

    """
    return (isinstance(obj, a_class))
