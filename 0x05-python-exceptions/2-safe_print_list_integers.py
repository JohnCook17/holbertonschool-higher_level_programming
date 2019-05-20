#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printnum = 0

    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            printnum += 1
        except:
            pass
        i += 1
    print('')
    return printnum
