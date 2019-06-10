#!/usr/bin/python3
"""A base class for the rest of the project

"""


class Base:
    """A base class for the rest of the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Inits the var id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
