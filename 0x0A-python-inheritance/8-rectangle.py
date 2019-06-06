#!/usr/bin/python3
"""makes a rectangle"""
bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(bg):
    """makes a rectangle
    """
    def __init__(self, width, height):
        """inits width and height

        Args:
            int: width the width
            int: height the height

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
