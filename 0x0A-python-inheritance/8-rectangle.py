#!/usr/bin/python3
bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(bg):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        bg.integer_validator(self.__width, "width", width)
        bg.integer_validator(self.__height, "height", height)
