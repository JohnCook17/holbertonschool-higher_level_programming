#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides every element of a matrix by a number div.

    Args:
        matrix (list): a matrix, a list of list.
        div (int) or (float): a number to divide by.

    Returns:
        list: a new matrix.

    Raises:
        Text goes here.

    """

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return list(map(lambda y: (list(map(lambda x: round((x / div), 2), y))), matrix))
