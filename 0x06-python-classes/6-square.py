#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__position = position
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0] and position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0] and position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        l = 0
        while l < self.__position[1]:
            print("")
            l += 1
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            print("")
        if self.__size == 0:
            print("")
