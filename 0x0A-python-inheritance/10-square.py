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
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area

        Returns: the area of a square

        """
        return self.__size * self.__size
