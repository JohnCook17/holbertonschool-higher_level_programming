#!/usr/bin/python3
"""A rectangle"""
bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(bg):
    """A rectangle

    Attributes:
        width: the width
        height: the height
    """
    def __init__(self, width, height):
        """init

        Args:
            width: width
            height: height

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """str

        Returns: the desired str output
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """area

        Returns: the area
        """
        answer = self.__width * self.__height
        return answer
