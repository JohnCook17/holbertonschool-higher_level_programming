#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    j = 0
    for value in matrix:
        for value2 in matrix[i]:
            print("{:d}".format(matrix[i][j]), end="")
            if j != len(matrix[i]) - 1:
                print(" ", end="")
            j += 1
        print("")
        j = 0
        i += 1
