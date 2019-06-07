#!/usr/bin/python3
def number_of_lines(filename=""):
    number = 0
    with open(filename, mode="r") as my_file:
        for line in my_file:
            number += 1
    return number
