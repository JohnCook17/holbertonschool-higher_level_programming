#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    number = 0
    print_lines = 0
    with open(filename, mode="r", encoding="utf-8") as my_file:
        for line in my_file:
            number += 1
        my_file.seek(0)
        if nb_lines <= 0 or nb_lines >= number:
            print(my_file.read())
        else:
            while print_lines < nb_lines:
                print(my_file.readline())
                print_lines += 1
