#!/usr/bin/python3
"""first name and last name"""

def say_my_name(first_name, last_name=""):
    """prints first name and optional last name.

    Args:
        first_name (str): first name
        last_name (str): optional last name

    Raises:
        TypeError

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
