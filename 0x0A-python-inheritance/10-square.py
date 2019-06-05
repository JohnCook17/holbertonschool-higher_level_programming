#!/usr/bin/python3
rec = __import__("9-rectangle").Rectangle


class Square(rec):
    def __init__(self, size):
        rec.integer_validator(self, "size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
