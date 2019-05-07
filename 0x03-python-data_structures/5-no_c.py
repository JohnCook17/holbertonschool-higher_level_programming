#!/usr/bin/python3
def no_c(my_string):
    newlst = my_string.split()
    newstr = ''
    i = 0
    j = 0
    while i < len(newlst):
        while j < len(newlst[i]):
            if newlst[i][j] != 'c' and newlst[i][j] != 'C':
                newstr += newlst[i][j]
            j += 1
        newstr += " "
        j = 0
        i += 1
    return newstr
