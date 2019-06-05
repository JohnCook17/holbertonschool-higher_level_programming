#!/usr/bin/python3
rec = __import__("9-rectangle").Rectangle


class Square(rec):
    def __init__(self, size):
        rec.integer_validator(self, "size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
