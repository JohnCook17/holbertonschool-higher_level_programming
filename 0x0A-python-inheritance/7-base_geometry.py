#!/usr/bin/python3
"""Basic Geometry"""


class BaseGeometry:
    """Basic Geometry

    methods:
        area: not implemented yet
        integer_validator: validates an int for use

    """
    def area(self):
        """unimplemented

        Raises: Exception its not implemented yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an int for use

            Raises:
                TypeError: must be an it
                ValueError: must be positive
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
