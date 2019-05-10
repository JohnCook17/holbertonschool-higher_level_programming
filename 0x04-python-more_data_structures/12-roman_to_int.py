#!/usr/bin/python3
def roman_to_int(roman_string):
    cases = {'I' : 1, 'IV' : 4, 'V' : 5, 'IX' : 9,
             'X' : 10, 'XL' : 40, 'L' : 50, 'XC' : 90,
             'C' : 100, 'CD' : 400, 'D' : 500, 'CM' : 900,
             'M' : 1000}
    num = 0
    j = 0
    l2 = ''
    for i in roman_string:
        l = roman_string[j]
        if j <= len(roman_string) +1:
            l2 = roman_string[j]
            res = l2 + l
        else:
            res = l
        if res in cases:
            num += cases[res]
            del res
            del l
            del l2
        elif res[-1] in cases:
            res2 = res[-1]
            if res2 in cases:
                num += cases[res2]
                del res
                del l
                del l2
        j += 1
    return num
