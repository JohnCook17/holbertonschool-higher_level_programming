#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    ret_list = []
    i = 0
    while length:
        if my_list[i] % 2 == 0:
            ret_list.append(True)
        else:
            ret_list.append(False)
        i += 1
        length -= 1
    return ret_list
