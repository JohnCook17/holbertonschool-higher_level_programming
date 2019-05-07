#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listcopy = my_list.copy()
    if idx < 0:
        return listcopy
    if idx > len(my_list):
        return listcopy
    listcopy[idx] = element
    return listcopy
