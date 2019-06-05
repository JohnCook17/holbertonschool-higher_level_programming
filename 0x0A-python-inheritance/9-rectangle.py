#!/usr/bin/python3
bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(bg):
    def __init__(self, width, height):
        bg.integer_validator(self, "width", width)
        bg.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        answer = self.__width * self.__height
        return answer
