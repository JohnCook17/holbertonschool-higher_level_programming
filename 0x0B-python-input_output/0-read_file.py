#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, mode='r', encoding="utf8") as my_file:
        print("{}".format(my_file.read()))
