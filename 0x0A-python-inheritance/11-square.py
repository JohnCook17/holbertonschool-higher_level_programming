#!/usr/bin/python3
"""square"""
rec = __import__("9-rectangle").Rectangle


class Square(rec):
    """square

    Args:
        int: size, the size of the square

    """
    def __init__(self, size):
        """init

        Args:
            int: size

        """
        rec.integer_validator(self, "size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """str

        Returns: the desired output is str format

        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """area

        Returns: the area of a square

        """
        return self.__size * self.__size
